# CISCO VIRTUAL INTERNSHIP 2026: INDIVIDUAL PROJECT CONTRIBUTION SUMMARY

**Candidate / Intern Name**: Nikhil Singh Chauhan  
**AICTE Registration ID**: STU666b367584a5f1718302325  
**College / Institution Name**: Indian Institute of Technology, Patna 
**Technology Track**: Cyber Security & Advanced Enterprise Networking  
**Project Title**: Secure Hybrid Data Center Network Architecture & Multi-Cloud Workload Protection  
**Submission Deadline**: 30th August 2026  
**File Naming Format Guide**: `Name-CollegeName-CyberSecurity-SummaryDocument.pdf` / `.docx`  

---

## 1. Project Overview & Context

The College IT Department initiated a major project to redesign the enterprise data center and cloud security posture. With academic and enterprise workloads spanning private on-premises infrastructure (Red Hat OpenShift, local databases) and public cloud environments (AWS EKS, RDS), our team was tasked with designing a secure, scalable, and resilient hybrid architecture.

My primary focus was engineering the **Cybersecurity & Network Architecture**, specifically solving the challenges of secure cross-boundary interconnectivity, Identity & Access Management (IAM), multi-tier VPC segmentation, Kubernetes microservice security, and Zero Trust remote faculty access.

---

## 2. Key Individual Contributions & Technical Deliverables

### A. Hybrid Interconnect & Perimeter Defense Engineering
- **Site-to-Site IPsec VPN Design**: Engineered the secure encrypted tunnel connecting the on-premises Cisco ASA 5506-X / Firepower perimeter firewall (`203.0.113.2`) to the Cloud Transit Gateway (`198.51.100.2`) using IKEv2, AES-256-GCM encryption, SHA-256 hashing, and Diffie-Hellman Group 14 with Perfect Forward Secrecy (PFS).
- **Identity NAT (NAT Exemption)**: Configured ASA NAT policies to exempt hybrid inter-datacenter traffic from port address translation, preserving internal source/destination IP headers for forensic auditing and Cisco Stealthwatch flow tracking.
- **Deep Packet Inspection & MPF**: Configured Modular Policy Framework (MPF) on the Cisco ASA to inspect stateful protocols (HTTP/HTTPS, DNS, SQL*Net, ICMP) and enforce Snort 3 Intrusion Prevention System (IPS) policies at the enterprise boundary.

### B. Identity & Access Management (IAM) & Least Privilege
- **OIDC Web Identity Federation (EKS IRSA)**: Architected the Kubernetes-to-AWS IAM bridge using IAM Roles for Service Accounts (IRSA), eliminating all hardcoded static API keys in container workloads.
- **RBAC & ABAC Policy Design**: Authored granular, least-privilege IAM policies restricting microservice pods to specific S3 research prefixes with mandatory AWS KMS Customer Managed Key (CMK) decryption rights.
- **Multi-Stakeholder Role Segregation**: Formulated distinct, segregated IAM roles for Application Developers, Kubernetes Platform Engineers, and Network Security Admins with mandatory MFA conditions.

### C. Cloud VPC Micro-Segmentation & Security Group Architecture
- **Hub-and-Spoke Transit Gateway Topology**: Designed the multi-VPC architecture using AWS Transit Gateway, eliminating full-mesh complexity and enabling centralized security policy enforcement.
- **3-Tier Subnet Isolation**: Partitioned the Cloud Production VPC into Public Ingress (Tier 1 - ALB/WAF), Private EKS Microservices (Tier 2 - No Public IP), and Isolated Database (Tier 3 - Zero Internet Routing).
- **SG-to-SG Referencing Matrix**: Implemented security group rules referencing peer Security Group IDs rather than CIDR blocks, preventing IP spoofing and mitigating lateral threat propagation.

### D. Kubernetes & Container Microservice Security
- **Calico CNI Zero-Trust Baseline**: Wrote declarative Kubernetes `NetworkPolicy` manifests establishing a default-deny posture across production namespaces, permitting only whitelisted ingress/egress flows between frontend, backend, and database tiers.
- **Pod Security Standards (PSS) Hardening**: Configured Kubernetes Pod Security Admission enforcing the `Restricted` profile (non-root execution UID 10001, read-only root filesystems, drop all capabilities, and default seccomp profiles).
- **Istio Service Mesh mTLS**: Configured Istio `PeerAuthentication` for STRICT mutual TLS 1.3 encryption and `AuthorizationPolicy` RBAC rules with SPIFFE cryptographic identity validation.

### E. Remote Faculty Access & Zero Trust (ZTNA)
- **Cisco AnyConnect SSL VPN & Duo MFA**: Configured SSL VPN remote access pools (`172.16.50.0/24`) integrated with Cisco Duo out-of-band push authentication.
- **Cisco ISE Dynamic Posture Assessment**: Designed endpoint compliance checks (verifying OS patch level, BitLocker/FileVault disk encryption, and active Cisco Secure Endpoint EDR) with automated quarantine redirection for non-compliant devices.
- **Split-Tunneling Optimization**: Established split-tunneling policies directing enterprise campus and cloud VPC traffic through the secure VPN while allowing direct internet breakout for general traffic.

### F. DevSecOps Pipeline & Multi-Stakeholder Collaboration
- **Automated Security Gates**: Designed the GitHub Actions CI/CD pipeline integrating Semgrep (SAST), Trivy (Container vulnerability scanning), Checkov/tfsec (IaC CIS benchmark scanning), and Cosign (cryptographic container image signing).
- **GitOps Deployment Gate**: Configured automated synchronization with ArgoCD requiring multi-stakeholder peer approval before deploying changes to production clusters.

---

## 3. Cisco Packet Tracer Simulation & CLI Configuration Artifacts

As part of the practical validation, I built and verified the complete network topology in Cisco Packet Tracer, authoring production-grade CLI configuration scripts for:
1. `01_Enterprise_Core_Router.ios`: OSPF routing, Inter-VLAN routing, NetFlow v9 export, ACLs.
2. `02_Enterprise_Firewall_ASA.cfg`: Inside/Outside/DMZ security zones, IKEv2 IPsec VPN, AnyConnect SSL VPN, MPF inspection.
3. `03_Enterprise_DC_Switch.ios`: 802.1Q trunks, Port Security (sticky MAC, violation shutdown), DHCP Snooping, Dynamic ARP Inspection (DAI), BPDU Guard.
4. `04_ISP_Internet_Router.ios`: Public Internet WAN routing, DNS server simulation.
5. `05_Cloud_Gateway_Router.ios`: Cloud Transit Gateway termination, IPsec crypto map, Cloud Security Group ACLs.
6. `06_Cloud_Workload_Switch.ios`: Cloud VPC subnet partitioning (Ingress, EKS, DB).

---

## 4. Learning Outcomes & Internship Experience

Through this Cisco Virtual Internship capstone project:
- Gained deep practical mastery of **Cisco Enterprise Security solutions** (ASA/Firepower, ISE, AnyConnect, Stealthwatch) and their integration with modern cloud-native architectures (AWS, Kubernetes, OpenShift).
- Mastered the principles of **Defense-in-Depth and Zero Trust Architecture (ZTA)** across physical, virtual, and containerized layers.
- Developed real-world expertise in **DevSecOps automation**, Policy-as-Code, and Infrastructure-as-Code (Terraform), preparing for enterprise cybersecurity and cloud networking roles.

---
**Candidate Signature**: _______________________  
**Date**: 24th August 2026
