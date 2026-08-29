# CISCO VIRTUAL INTERNSHIP 2026: CYBER SECURITY PROJECT

## Project Title: Secure Hybrid Data Center Network Architecture & Multi-Cloud Workload Protection

---

### Project Overview & Problem Statement
This project delivers an enterprise-grade cybersecurity architecture for a hybrid data center and multi-cloud environment as required by the **Cisco Virtual Internship 2026 (AICTE & Cisco Networking Academy)** program.

The architecture securely interconnects on-premises enterprise data center infrastructure (Red Hat OpenShift, local relational databases) with public cloud environments (AWS EKS, RDS, Transit Gateway), enforcing Zero-Trust segmentation, least-privilege IAM, container security, and remote faculty access.

---

### Key Technical Highlights
- **Hybrid Interconnect & Perimeter Defense**: High-throughput Site-to-Site IPsec VPN (IKEv2, AES-256-GCM, SHA-256, DH Group 14) terminated on a Cisco ASA 5506-X / Firepower Threat Defense firewall with Identity NAT and Snort 3 IPS deep inspection.
- **Identity & Access Management (IAM)**: Centralized SSO using Cisco Duo MFA + Cisco ISE federated with AWS IAM via OIDC (EKS IAM Roles for Service Accounts - IRSA), completely removing static cloud credentials.
- **Cloud Network Micro-Segmentation**: AWS Transit Gateway Hub-and-Spoke topology with 3-tier subnets (Public Ingress ALB, Private EKS Microservices, and Isolated Database with zero internet routing) utilizing stateful Security Group-to-Security Group referencing rules to prevent lateral movement.
- **Kubernetes & Microservice Hardening**: Calico CNI default-deny network policies, Kubernetes Restricted Pod Security Standards (non-root, read-only rootfs, drop ALL capabilities), and Istio STRICT mutual TLS (mTLS 1.3) with SPIFFE cryptographic X.509 identity.
- **Zero Trust Remote Faculty Access (ZTNA)**: Cisco AnyConnect / Secure Client SSL VPN with Cisco Duo MFA and dynamic Cisco ISE posture assessment (validating OS patch levels, BitLocker disk encryption, and active Cisco Secure Endpoint EDR).
- **DevSecOps Pipeline & Governance**: Automated GitHub Actions CI/CD pipeline enforcing SAST (Semgrep), container CVE scanning (Trivy), IaC security scanning (Checkov), and cryptographic image signing (Cosign) with GitOps (ArgoCD) production deployment gates.

---

### Repository Structure & Deliverables

```
d:/PROJECTS/CISCO/
│
├── README.md                                  # Repository overview & quick start
│
├── docs/                                      # Master Documentation & Submission Files
│   ├── CISCO_CYBERSECURITY_HYBRID_DATACENTER_PROJECT_REPORT.md  # Master technical report (Markdown)
│   ├── STUDENT_CONTRIBUTION_SUMMARY.md        # Individual contribution summary (Markdown)
│   ├── CISCO_PACKET_TRACER_LAB_GUIDE.md       # Step-by-step Packet Tracer build & testing guide
│   ├── Cisco_Cybersecurity_Internship_Report.docx # Formatted Word report (.docx)
│   ├── Cisco_Cybersecurity_Internship_Report.pdf  # Publication-ready PDF report (.pdf)
│   └── Student_Contribution_Summary.pdf       # Submission-ready individual summary (.pdf)
│
├── packet_tracer_configs/                     # Cisco Packet Tracer Device CLI Scripts
│   ├── 01_Enterprise_Core_Router.ios          # Core Router (OSPF, Inter-VLAN, NetFlow, ACLs)
│   ├── 02_Enterprise_Firewall_ASA.cfg         # ASA Firewall (Inside/Outside/DMZ, IPsec VPN, NAT)
│   ├── 03_Enterprise_DC_Switch.ios            # DC Switch (VLANs, Trunks, Port Security, Snooping)
│   ├── 04_ISP_Internet_Router.ios             # ISP WAN Backbone Router
│   ├── 05_Cloud_Gateway_Router.ios            # Cloud Transit Gateway (IPsec Tunnel, Cloud SGs)
│   └── 06_Cloud_Workload_Switch.ios           # Cloud VPC Subnet Switch
│
├── infrastructure_as_code/                    # Production-Ready IaC & Security Policies
│   ├── terraform/                             # AWS Transit Gateway, VPCs, Subnets, SGs, IAM
│   │   ├── main.tf
│   │   ├── security_groups.tf
│   │   ├── iam_roles.tf
│   │   └── variables.tf
│   └── kubernetes_security/                   # Kubernetes & Calico Security Manifests
│       ├── 01_calico_default_deny.yaml        # Zero-Trust default deny network policy
│       ├── 02_microservice_segmentation.yaml  # Microservice tier ingress/egress rules
│       ├── 03_pod_security_admission.yaml     # Restricted pod security standards
│       └── 04_istio_mtls_policy.yaml          # Istio STRICT mTLS & authorization RBAC
│
├── devsecops/                                 # DevSecOps & Governance Automation
│   └── ci_cd_pipeline.yml                     # GitHub Actions workflow (SAST, Trivy, Checkov)
│
└── scripts/                                   # Automation & Document Generator Scripts
    ├── generate_docx_report.py                # Compiles Word Document (.docx)
    └── generate_pdf_report.py                 # Compiles PDF Documents (.pdf)
```

---

### Submission Instructions for NetAcad / AICTE Portal

1. **Submission Form URL**: [https://forms.gle/3rh45ov9hBhJsg14A](https://forms.gle/3rh45ov9hBhJsg14A)
2. **Deadline**: 30th August 2026
3. **File Naming Format Guidelines**:
   - **Packet Tracer File**: `YourName-YourCollege-CyberSecurity.pkt`
   - **Summary Document**: `YourName-YourCollege-CyberSecurity-SummaryDocument.pdf` (or `.docx`)
4. **Certificate & AICTE ID**: Ensure your AICTE Registration ID is accurately entered during submission.

---
*Developed for Cisco Virtual Internship 2026.*
