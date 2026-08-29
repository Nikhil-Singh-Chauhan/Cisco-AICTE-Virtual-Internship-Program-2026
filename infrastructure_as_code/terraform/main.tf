# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Terraform Infrastructure as Code: Secure Multi-VPC Hybrid Cloud Architecture
# Module: AWS Transit Gateway, Hub & Spoke VPCs, Subnets, and Site-to-Site VPN
# ==============================================================================

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project     = "Cisco-Cybersecurity-Hybrid-DC"
      Environment = "Production"
      ManagedBy   = "Terraform"
      Compliance  = "CIS-AWS-Foundations-v2.0"
    }
  }
}

# --- AWS Transit Gateway (TGW) Hub ---
resource "aws_ec2_transit_gateway" "hybrid_tgw" {
  description                     = "Central Hub Transit Gateway for Hybrid DC Interconnect"
  amazon_side_asn                 = 64512
  auto_accept_shared_attachments  = "disable"
  default_route_table_association = "disable"
  default_route_table_propagation = "disable"
  dns_support                     = "enable"
  vpn_ecmp_support                = "enable"

  tags = {
    Name = "tgw-cisco-hybrid-hub"
  }
}

# --- Customer Gateway (Cisco ASA Firewall at On-Prem DC) ---
resource "aws_customer_gateway" "onprem_cisco_asa" {
  bgp_asn    = 65000
  ip_address = var.onprem_asa_public_ip # 203.0.113.2
  type       = "ipsec.1"

  tags = {
    Name = "cgw-onprem-cisco-asa-5506"
  }
}

# --- Site-to-Site IPsec VPN to On-Premise Data Center ---
resource "aws_vpn_connection" "hybrid_ipsec_vpn" {
  transit_gateway_id  = aws_ec2_transit_gateway.hybrid_tgw.id
  customer_gateway_id = aws_customer_gateway.onprem_cisco_asa.id
  type                = "ipsec.1"
  static_routes_only  = false

  tunnel1_inside_cidr   = "169.254.10.0/30"
  tunnel1_preshared_key = var.vpn_preshared_key
  tunnel1_phase1_encryption_algorithms = ["AES256"]
  tunnel1_phase1_integrity_algorithms  = ["SHA2-256"]
  tunnel1_phase1_dh_group_numbers      = [14]
  tunnel1_phase2_encryption_algorithms = ["AES256"]
  tunnel1_phase2_integrity_algorithms  = ["SHA2-256"]
  tunnel1_phase2_dh_group_numbers      = [14]

  tags = {
    Name = "vpn-hybrid-cisco-dc"
  }
}

# --- Production Workload VPC ---
resource "aws_vpc" "prod_workload_vpc" {
  cidr_block           = "172.20.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "vpc-cisco-prod-workloads"
  }
}

# --- Multi-Tier Subnet Segmentation ---
# 1. Ingress Public Subnets (For ALB & Firewalls)
resource "aws_subnet" "public_ingress_1a" {
  vpc_id                  = aws_vpc.prod_workload_vpc.id
  cidr_block              = "172.20.1.0/24"
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = false

  tags = {
    Name = "subnet-prod-ingress-az1a"
    Tier = "Public-Ingress"
  }
}

# 2. Application / EKS Microservice Private Subnets (No Direct Internet Access)
resource "aws_subnet" "app_microservices_1a" {
  vpc_id            = aws_vpc.prod_workload_vpc.id
  cidr_block        = "172.20.2.0/24"
  availability_zone = "${var.aws_region}a"

  tags = {
    Name                     = "subnet-prod-eks-microservices-az1a"
    Tier                     = "Private-Application"
    "kubernetes.io/role/elb" = "1"
  }
}

# 3. Database / Persistence Isolated Subnets (Zero Outbound Egress)
resource "aws_subnet" "db_isolated_1a" {
  vpc_id            = aws_vpc.prod_workload_vpc.id
  cidr_block        = "172.20.3.0/24"
  availability_zone = "${var.aws_region}a"

  tags = {
    Name = "subnet-prod-database-isolated-az1a"
    Tier = "Isolated-Persistence"
  }
}

# --- Transit Gateway VPC Attachment ---
resource "aws_ec2_transit_gateway_vpc_attachment" "prod_vpc_tgw_attachment" {
  transit_gateway_id = aws_ec2_transit_gateway.hybrid_tgw.id
  vpc_id             = aws_vpc.prod_workload_vpc.id
  subnet_ids         = [aws_subnet.app_microservices_1a.id]

  tags = {
    Name = "tgw-attach-prod-vpc"
  }
}

# --- VPC Route Tables & Hybrid Routing ---
resource "aws_route_table" "app_private_rt" {
  vpc_id = aws_vpc.prod_workload_vpc.id

  # Route On-Premises Campus/DC Traffic (10.10.0.0/16) to Transit Gateway
  route {
    cidr_block         = "10.10.0.0/16"
    transit_gateway_id = aws_ec2_transit_gateway.hybrid_tgw.id
  }

  tags = {
    Name = "rt-prod-app-private"
  }
}

resource "aws_route_table_association" "app_private_assoc" {
  subnet_id      = aws_subnet.app_microservices_1a.id
  route_table_id = aws_route_table.app_private_rt.id
}

# Database Route Table (Strictly isolated within VPC, no internet or external routes)
resource "aws_route_table" "db_isolated_rt" {
  vpc_id = aws_vpc.prod_workload_vpc.id

  tags = {
    Name = "rt-prod-db-isolated"
  }
}

resource "aws_route_table_association" "db_isolated_assoc" {
  subnet_id      = aws_subnet.db_isolated_1a.id
  route_table_id = aws_route_table.db_isolated_rt.id
}

# --- VPC Flow Logs for Cisco Stealthwatch & SIEM Analytics ---
resource "aws_flow_log" "prod_vpc_flow_logs" {
  iam_role_arn    = aws_iam_role.vpc_flow_log_role.arn
  log_destination = aws_cloudwatch_log_group.vpc_flow_logs.arn
  traffic_type    = "ALL"
  vpc_id          = aws_vpc.prod_workload_vpc.id
}

resource "aws_cloudwatch_log_group" "vpc_flow_logs" {
  name              = "/aws/vpc/flow-logs/cisco-hybrid-prod"
  retention_in_days = 90
}
