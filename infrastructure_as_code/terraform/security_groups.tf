# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Terraform Infrastructure as Code: Least-Privilege Security Groups
# Architecture: SG-to-SG Referencing to prevent lateral movement and CIDR spoofing
# ==============================================================================

# --- 1. Public Application Load Balancer Security Group ---
resource "aws_security_group" "alb_security_group" {
  name        = "sg-prod-ingress-alb"
  description = "Allows inbound HTTPS from internet/clients and forwards to microservices"
  vpc_id      = aws_vpc.prod_workload_vpc.id

  ingress {
    description = "Allow HTTPS from trusted enterprise & internet users"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description     = "Forward traffic only to Kubernetes Microservice Nodes"
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_microservices_sg.id]
  }

  tags = {
    Name = "sg-prod-ingress-alb"
  }
}

# --- 2. Kubernetes / EKS Microservice Worker Nodes Security Group ---
resource "aws_security_group" "eks_microservices_sg" {
  name        = "sg-prod-eks-microservices"
  description = "Security group for EKS worker nodes running hybrid microservices"
  vpc_id      = aws_vpc.prod_workload_vpc.id

  ingress {
    description     = "Allow traffic strictly from ALB on application port"
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_security_group.id]
  }

  ingress {
    description = "Allow internal hybrid RPC/REST from On-Premises OpenShift (10.10.30.0/24)"
    from_port   = 8443
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = ["10.10.30.0/24"]
  }

  ingress {
    description = "Allow Faculty AnyConnect VPN users for academic microservice tools"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["172.16.50.0/24", "10.10.10.0/24"]
  }

  # Node-to-Node Inter-Pod Communication for Kubernetes CNI
  ingress {
    description = "Allow inter-pod cluster communication within the EKS node group"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    self        = true
  }

  egress {
    description     = "Allow egress strictly to RDS Database on PostgreSQL port"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.database_isolated_sg.id]
  }

  egress {
    description = "Allow egress back to On-Premise Data Center Oracle/Postgres DB (10.10.30.0/24)"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["10.10.30.0/24"]
  }

  egress {
    description = "Allow secure HTTPS to AWS VPC Interface Endpoints (S3, ECR, KMS, SecretsManager)"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["172.20.0.0/16"]
  }

  tags = {
    Name = "sg-prod-eks-microservices"
  }
}

# --- 3. Isolated Database Tier Security Group ---
resource "aws_security_group" "database_isolated_sg" {
  name        = "sg-prod-database-isolated"
  description = "Strictly isolated security group for relational databases"
  vpc_id      = aws_vpc.prod_workload_vpc.id

  ingress {
    description     = "Allow PostgreSQL access strictly from authorized EKS Microservices SG"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_microservices_sg.id]
  }

  ingress {
    description = "Allow Database Admin queries strictly from On-Premises Admin Jumpbox (10.10.99.10)"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["10.10.99.10/32"]
  }

  # Zero Egress Rule: Database has NO outbound connections (Prevents data exfiltration)
  tags = {
    Name = "sg-prod-database-isolated"
  }
}

# --- 4. AWS PrivateLink / VPC Interface Endpoints Security Group ---
resource "aws_security_group" "vpce_security_group" {
  name        = "sg-prod-vpc-endpoints"
  description = "Security group for AWS PrivateLink interface endpoints"
  vpc_id      = aws_vpc.prod_workload_vpc.id

  ingress {
    description     = "Allow HTTPS from EKS Microservices for Secrets and Container Images"
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_microservices_sg.id]
  }

  tags = {
    Name = "sg-prod-vpc-endpoints"
  }
}
