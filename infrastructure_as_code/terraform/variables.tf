# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Terraform Input Variables & Outputs
# ==============================================================================

variable "aws_region" {
  type        = string
  description = "AWS Deployment Region"
  default     = "us-east-1"
}

variable "aws_account_id" {
  type        = string
  description = "Target AWS Account ID"
  default     = "123456789012"
}

variable "onprem_asa_public_ip" {
  type        = string
  description = "Public IP address of Enterprise On-Premises Cisco ASA Firewall"
  default     = "203.0.113.2"
}

variable "vpn_preshared_key" {
  type        = string
  description = "Pre-shared key for Site-to-Site IPsec VPN tunnel"
  default     = "CiscoNetAcadHybridSecret2026!"
  sensitive   = true
}

variable "eks_cluster_oidc_id" {
  type        = string
  description = "OIDC Provider ID for EKS Cluster"
  default     = "EXAMPLED5B9A61726330C3868246E0EE"
}
