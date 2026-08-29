# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Terraform Infrastructure as Code: IAM Architecture & Least-Privilege RBAC
# Features: EKS IRSA (OIDC), Multi-Stakeholder Roles, KMS Encryption, S3 Bucket Policies
# ==============================================================================

# --- KMS Customer Managed Key (CMK) for Envelope Encryption ---
resource "aws_kms_key" "hybrid_dc_kms_key" {
  description             = "KMS Key for encrypting hybrid data center volumes, S3, and secrets"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  tags = {
    Name = "kms-cisco-hybrid-key"
  }
}

# --- EKS OIDC Identity Provider (IAM Roles for Service Accounts - IRSA) ---
# Allows Kubernetes Pods to assume IAM roles without long-lived static API keys
resource "aws_iam_role" "eks_microservice_pod_role" {
  name = "role-eks-microservice-least-privilege"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = "arn:aws:iam::${var.aws_account_id}:oidc-provider/oidc.eks.${var.aws_region}.amazonaws.com/id/${var.eks_cluster_oidc_id}"
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "oidc.eks.${var.aws_region}.amazonaws.com/id/${var.eks_cluster_oidc_id}:sub" : "system:serviceaccount:production:academic-microservice-sa",
            "oidc.eks.${var.aws_region}.amazonaws.com/id/${var.eks_cluster_oidc_id}:aud" : "sts.amazonaws.com"
          }
        }
      }
    ]
  })

  tags = {
    Name = "role-eks-microservice-pod"
  }
}

# Least-Privilege IAM Policy for Microservice (Access only to specific S3 prefix & KMS decrypt)
resource "aws_iam_policy" "microservice_data_access_policy" {
  name        = "policy-eks-microservice-data-access"
  description = "Granular access policy for academic microservices"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowResearchBucketReadWrite"
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.research_repository.arn,
          "${aws_s3_bucket.research_repository.arn}/datasets/*"
        ]
      },
      {
        Sid    = "AllowKmsDecryption"
        Effect = "Allow"
        Action = [
          "kms:Decrypt",
          "kms:GenerateDataKey"
        ]
        Resource = aws_kms_key.hybrid_dc_kms_key.arn
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_pod_policy" {
  role       = aws_iam_role.eks_microservice_pod_role.name
  policy_arn = aws_iam_policy.microservice_data_access_policy.arn
}

# --- Secure S3 Research Repository Bucket ---
resource "aws_s3_bucket" "research_repository" {
  bucket        = "cisco-hybrid-academic-research-repo-${var.aws_account_id}"
  force_destroy = false

  tags = {
    Name = "s3-academic-research-repository"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "s3_encryption" {
  bucket = aws_s3_bucket.research_repository.id

  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.hybrid_dc_kms_key.arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block_public" {
  bucket                  = aws_s3_bucket.research_repository.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# --- Stakeholder IAM Roles & Segregation of Duties ---

# 1. Application Developer Role (Limited to Dev namespace and non-prod resources)
resource "aws_iam_role" "app_developer_role" {
  name = "role-stakeholder-app-developer"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = "arn:aws:iam::${var.aws_account_id}:root" }
        Action    = "sts:AssumeRole"
        Condition = {
          Bool = { "aws:MultiFactorAuthPresent" : "true" }
        }
      }
    ]
  })
}

# 2. Kubernetes Platform Engineer Role (Cluster management via GitOps)
resource "aws_iam_role" "platform_engineer_role" {
  name = "role-stakeholder-platform-engineer"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = "arn:aws:iam::${var.aws_account_id}:root" }
        Action    = "sts:AssumeRole"
        Condition = {
          Bool = { "aws:MultiFactorAuthPresent" : "true" }
        }
      }
    ]
  })
}

# 3. Network Security Engineer Role (Transit Gateway, VPN, Security Groups, Flow Logs)
resource "aws_iam_role" "network_security_role" {
  name = "role-stakeholder-network-security"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = "arn:aws:iam::${var.aws_account_id}:root" }
        Action    = "sts:AssumeRole"
        Condition = {
          Bool = { "aws:MultiFactorAuthPresent" : "true" }
        }
      }
    ]
  })
}

# --- VPC Flow Log IAM Role ---
resource "aws_iam_role" "vpc_flow_log_role" {
  name = "role-cisco-vpc-flow-logs"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "vpc-flow-logs.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "vpc_flow_log_policy" {
  name = "policy-cisco-vpc-flow-logs"
  role = aws_iam_role.vpc_flow_log_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}
