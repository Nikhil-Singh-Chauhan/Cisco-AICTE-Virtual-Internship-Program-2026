# CISCO VIRTUAL INTERNSHIP 2026: CYBER SECURITY CAPSTONE PROJECT

# Secure Hybrid Data Center Network Architecture & Multi-Cloud Workload Protection

---

**Program**: Cisco Virtual Internship 2026 (AICTE & Cisco Networking Academy)  
**Track**: Cyber Security & Advanced Enterprise Infrastructure  
**Problem Statement**: Enterprise Hybrid Data Center Security, IAM Architecture, VPC Micro-Segmentation, Kubernetes Security & Remote Faculty Access  
**Author / Intern**: Cisco Cybersecurity Student Intern  
**Submission Date**: August 2026  
**Document Classification**: Confidential / Technical Architecture & Implementation Report  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement & Project Objectives](#2-problem-statement--project-objectives)
3. [End-to-End Hybrid Architecture Design](#3-end-to-end-hybrid-architecture-design)
   - 3.1 Network Topology & Interconnect Overview
   - 3.2 IP Addressing & Subnet Allocation Matrix
   - 3.3 Perimeter & Edge Security Architecture
4. [Identity & Access Management (IAM) Architecture](#4-identity--access-management-iam-architecture)
   - 4.1 Centralized Identity Provider & SSO (Cisco Duo + Cisco ISE + AWS IAM)
   - 4.2 Role-Based (RBAC) and Attribute-Based (ABAC) Access Control
   - 4.3 EKS IAM Roles for Service Accounts (IRSA) & OIDC Federation
   - 4.4 Privileged Access Management (PAM) & Just-In-Time (JIT) Elevation
5. [Cloud Network Segmentation & Security Group Architecture](#5-cloud-network-segmentation--security-group-architecture)
   - 5.1 AWS Transit Gateway Hub-and-Spoke Topology
   - 5.2 Multi-Tier Subnet Isolation (Public ALB, Private App, Isolated DB)
   - 5.3 Stateful Security Groups Matrix (SG-to-SG Referencing)
   - 5.4 Stateless Network Access Control Lists (NACLs)
6. [Container & Kubernetes Microservice Security (OpenShift / EKS)](#6-container--kubernetes-microservice-security-openshift--eks)
   - 6.1 Container Network Interface (Calico CNI) Default-Deny Policies
   - 6.2 Pod Security Standards (PSS) & Runtime Hardening
   - 6.3 Istio Service Mesh & Mutual TLS (mTLS 1.3)
   - 6.4 Dynamic Secrets Injection & Image Provenance (Cosign / Trivy)
7. [Secure Hybrid Workforce & Remote Faculty Access](#7-secure-hybrid-workforce--remote-faculty-access)
   - 7.1 Zero Trust Network Access (ZTNA) Architecture
   - 7.2 Cisco AnyConnect / Secure Client & Duo MFA Integration
   - 7.3 Cisco ISE Dynamic Posture Assessment & Health Checks
   - 7.4 Optimized Split-Tunneling Policy
8. [Multi-Stakeholder Collaboration & DevSecOps Governance](#8-multi-stakeholder-collaboration--devsecops-governance)
   - 8.1 Stakeholder Responsibility Matrix (RACI)
   - 8.2 GitOps Infrastructure-as-Code Deployment Workflow
   - 8.3 Automated DevSecOps Pipeline & Security Gates
9. [Threat Modeling, Blast Radius Containment & Defense-in-Depth](#9-threat-modeling-blast-radius-containment--defense-in-depth)
   - 9.1 STRIDE Threat Analysis
   - 9.2 Blast Radius Containment & Lateral Movement Mitigation
   - 9.3 Telemetry, Anomaly Detection & Cisco Stealthwatch Integration
   - 9.4 Centralized SIEM & Cisco SecureX Visibility
10. [Engineering Evaluation: Simplicity, Security & Scalability](#10-engineering-evaluation-simplicity-security--scalability)
11. [Cisco Packet Tracer Implementation & CLI Verification Guide](#11-cisco-packet-tracer-implementation--cli-verification-guide)
12. [Conclusion & Future Roadmap](#12-conclusion--future-roadmap)

---

## 1. Executive Summary

Modern enterprise and academic institutions are undergoing a fundamental transformation from monolithic on-premises architectures to distributed **hybrid multi-cloud ecosystems**. Today's critical applications and research workloads no longer reside solely within a private data center; instead, they span private on-premise clusters (e.g., Red Hat OpenShift, VMware) and elastic public cloud environments (e.g., Amazon Web Services EKS, Microsoft Azure AKS, Google Cloud GKE).

While this hybrid paradigm unlocks unprecedented agility, rapid scaling, and resilient academic collaboration, it introduces significant cybersecurity challenges:
1. **Perimeter Dissolution**: Data actively traverses public and hybrid interconnects between private data centers and cloud VPCs, exposing traffic to interception and lateral infiltration if improperly segmented.
2. **Identity Fragmentation**: Multiple teams (Application Developers, Network Designers, Kubernetes Platform Engineers, and Remote Faculty) interact with hybrid resources using disparate authentication mechanisms.
3. **Container & Microservice Attack Surface**: Containerized workloads running on distributed Kubernetes clusters introduce inter-pod lateral movement risks, privileged container escapes, and vulnerable software dependencies.
4. **Remote Workforce Exposure**: Faculty members requiring seamless access to research repositories and internal computing clusters from campus or home networks create attack vectors via compromised endpoints.

This project delivers an enterprise-grade, defense-in-depth **Secure Hybrid Data Center Network Architecture** designed to balance **simplicity, rock-solid security, and linear scalability**. Leveraging industry-standard Cisco security frameworks (Cisco ASA/Firepower, Cisco ISE, Cisco Duo, Cisco Stealthwatch/Secure Network Analytics) integrated with cloud-native security controls (AWS Transit Gateway, SG-to-SG referencing, IAM OIDC federation, Calico CNI default-deny, and Istio mTLS), this architecture ensures that a breach of any single workload is immediately contained, logged, and neutralized without compromising the broader enterprise ecosystem.

---

## 2. Problem Statement & Project Objectives

### 2.1 The Problem Context
Following a security audit, the College IT Department tasked our engineering team with redesigning the data center and multi-cloud network security posture. The core operational realities include:
- **Hybrid Workloads**: High-value teaching tools, research databases, and administrative portals operate across both the on-premises private data center and public cloud infrastructure.
- **Microservices & Kubernetes**: Applications are containerized and orchestrated using Kubernetes (OpenShift on-premise and EKS in the cloud).
- **Multi-Stakeholder Ecosystem**: Deploying new applications involves cross-functional collaboration between application developers, network designers, and platform engineers.
- **Remote & Hybrid Faculty**: Faculty members need uninterrupted, high-speed, secure access to hybrid applications from anywhere (home or campus).

### 2.2 Core Technical Objectives
1. **Design a Resilient Hybrid Interconnect**: Build a high-throughput, encrypted Site-to-Site IPsec VPN (IKEv2, AES-256-GCM) with dynamic routing and perimeter firewall inspection connecting the on-premise data center to the cloud.
2. **Formulate a Unified IAM Architecture**: Eliminate static API credentials through OIDC Web Identity Federation (IAM Roles for Service Accounts - IRSA), Least Privilege Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), and Multi-Factor Authentication (MFA).
3. **Implement Cloud VPC Micro-Segmentation**: Design a Hub-and-Spoke VPC architecture via AWS Transit Gateway, with multi-tier isolated subnets and stateful Security Group-to-Security Group referencing rules to eliminate lateral movement.
4. **Harden Kubernetes & Microservices**: Establish a Zero-Trust pod communication baseline using Calico CNI default-deny policies, Istio STRICT mutual TLS (mTLS 1.3), and Pod Security Standards (Restricted Profile).
5. **Enable Secure Zero-Trust Remote Access (ZTNA)**: Deploy Cisco AnyConnect SSL VPN integrated with Cisco Duo MFA and Cisco ISE dynamic endpoint posture assessment for faculty.
6. **Establish DevSecOps Pipeline Governance**: Implement automated security validation gates (SAST, Container CVE scanning, IaC Checkov linting, and GitOps ArgoCD synchronization) for seamless multi-stakeholder collaboration.

---

## 3. End-to-End Hybrid Architecture Design

### 3.1 Network Topology & Interconnect Overview
The architecture is divided into four distinct security zones:
1. **Enterprise Campus & Private Data Center (On-Premises)**: Hosts legacy systems, primary relational databases, and an on-premise Red Hat OpenShift container cluster. Protected by Cisco Catalyst Core/Distribution switches and a perimeter Cisco ASA 5506-X / Firepower Threat Defense (FTD) firewall.
2. **Public WAN / Internet Transit**: Simulates the ISP carrier network providing BGP transit and public internet routing.
3. **Cloud Ingress & Transit Hub (AWS Transit Gateway)**: Central routing and inspection hub connecting multiple spoke VPCs to the on-premise data center via encrypted IPsec VPN tunnels.
4. **Cloud Workload VPCs (Production EKS & Persistence)**: Multi-tier segmented VPCs hosting scalable cloud-native microservices, elastic container workers, and managed database clusters (AWS Aurora / RDS).

```
+---------------------------------------------------------------------------------------------------------+
|                                    ENTERPRISE HYBRID NETWORK TOPOLOGY                                   |
+---------------------------------------------------------------------------------------------------------+
|                                                                                                         |
|  +---------------------------------------------------+       +---------------------------------------+  |
|  |           ON-PREMISES CAMPUS & DATA CENTER        |       |          PUBLIC INTERNET / WAN        |  |
|  |                                                   |       |                                       |  |
|  |  [Faculty LAN]      [Staff LAN]    [Admin Mgmt]   |       |             +-----------------+       |  |
|  |  10.10.10.0/24     10.10.20.0/24   10.10.99.0/24  |       |             | ISP Router      |       |  |
|  |         \                |              /         |       |             | 203.0.113.1     |       |  |
|  |          +---------------+-------------+          |       |             +--------+--------+       |  |
|  |                          |                        |       |                      |                |  |
|  |             +------------+------------+           |       |                      |                |  |
|  |             | Cisco L2/L3 DC Switch   |           |       |                      |                |  |
|  |             | (VLANs, DAI, Snooping)  |           |       |                      |                |  |
|  |             +------------+------------+           |       |                      |                |  |
|  |                          |                        |       |                      |                |  |
|  |             +------------+------------+           |       |                      |                |  |
|  |             | ENT Core Router (OSPF)  |           |       |                      |                |  |
|  |             +------------+------------+           |       |                      |                |  |
|  |                          | 10.10.0.0/30           |       |                      |                |  |
|  |             +------------+------------+           |       |                      |                |  |
|  |             | Cisco ASA / Firepower   |-----------+-------+----------------------+                |  |
|  |             | Outside: 203.0.113.2    |  (IPsec VPN: IKEv2 / AES-256-GCM / DH 14)                 |  |
|  |             +-------------------------+                   |                      |                |  |
|  |                          |                                |                      |                |  |
|  |  +-----------------------+---------------------+          |                      |                |  |
|  |  | On-Prem OpenShift & DB: 10.10.30.0/24       |          |                      |                |  |
|  |  +---------------------------------------------+          |                      |                |  |
|  +---------------------------------------------------+       +----------------------+----------------+  |
|                                                                                     |                   |
|                                                                                     |                   |
|  +----------------------------------------------------------------------------------+----------------+  |
|  |                              PUBLIC CLOUD (AWS / MULTI-CLOUD HUB & SPOKE)                          |  |
|  |                                                                                                    |  |
|  |                     +---------------------------------------------------------+                    |  |
|  |                     | AWS Transit Gateway (TGW) Hub / Cloud Gateway Router    |                    |  |
|  |                     | Outside WAN: 198.51.100.2 | Tunnel Interface: 169.254.10.0/30                |  |
|  |                     +----------------------------+----------------------------+                    |  |
|  |                                                  |                                                 |  |
|  |                     +----------------------------+----------------------------+                    |  |
|  |                     | PRODUCTION WORKLOAD VPC (CIDR: 172.20.0.0/16)           |                    |  |
|  |                     |                                                         |                    |  |
|  |                     |  [Tier 1: Ingress Public Subnet]                        |                    |  |
|  |                     |  - Subnet: 172.20.1.0/24                                |                    |  |
|  |                     |  - Application Load Balancers (ALB) / WAF               |                    |  |
|  |                     |                       | (Port 8080 - SG Ref)            |                    |  |
|  |                     |  [Tier 2: EKS Microservices Private Subnet]             |                    |  |
|  |                     |  - Subnet: 172.20.2.0/24 (Zero Internet Ingress)        |                    |  |
|  |                     |  - Container Worker Nodes (Calico + Istio mTLS)         |                    |  |
|  |                     |                       | (Port 5432 - SG Ref)            |                    |  |
|  |                     |  [Tier 3: Database Isolated Persistence Subnet]         |                    |  |
|  |                     |  - Subnet: 172.20.3.0/24 (Zero Internet Ingress/Egress) |                    |  |
|  |                     |  - AWS Aurora / PostgreSQL / Research DB                |                    |  |
|  |                     +---------------------------------------------------------+                    |  |
|  +----------------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------------+
```

### 3.2 IP Addressing & Subnet Allocation Matrix

| Network Segment | Subnet CIDR | VLAN / ID | Purpose & Security Classification |
| :--- | :--- | :--- | :--- |
| **Enterprise Core Transit** | `10.10.0.0/30` | P2P | Point-to-point link between Core Router and ASA Inside interface |
| **Faculty Workstations** | `10.10.10.0/24` | VLAN 10 | On-premise faculty desktops, laptops; authenticated via 802.1X |
| **Staff & Students LAN** | `10.10.20.0/24` | VLAN 20 | General campus traffic; strictly restricted from data center DBs |
| **On-Prem Data Center** | `10.10.30.0/24` | VLAN 30 | OpenShift container nodes, local identity servers, research DBs |
| **Network Management** | `10.10.99.0/24` | VLAN 99 | Out-of-band management for routers, switches, ASA, and jumpboxes |
| **Remote AnyConnect VPN** | `172.16.50.0/24` | SSL VPN | Dynamic IP pool for remote faculty connecting via Cisco Secure Client |
| **Enterprise WAN Edge** | `203.0.113.0/30` | Outside | Public IP interface on Cisco ASA (`203.0.113.2`) facing ISP |
| **Cloud WAN Edge** | `198.51.100.0/30` | WAN GW | Public IP interface on Cloud Transit Gateway (`198.51.100.2`) |
| **Cloud Ingress Subnet** | `172.20.1.0/24` | Tier 1 | Public Load Balancers (ALB), TLS termination, AWS WAF |
| **Cloud EKS App Subnet** | `172.20.2.0/24` | Tier 2 | Kubernetes microservices; private routing only; no public IPs |
| **Cloud Database Subnet**| `172.20.3.0/24` | Tier 3 | Relational database instances; strictly isolated; zero internet routing |

### 3.3 Perimeter & Edge Security Architecture
- **Site-to-Site Encrypted Overlay**: All data leaving the private data center for the cloud is encapsulated in an **IPsec ESP tunnel using IKEv2**. Encryption uses **AES-256-GCM** with **SHA-256** hashing and **Diffie-Hellman Group 14** (2048-bit MODP), ensuring cryptographic confidentiality and Perfect Forward Secrecy (PFS).
- **Identity NAT (NAT Exemption)**: Traffic between `10.10.0.0/16` and `172.20.0.0/16` bypasses standard internet PAT, maintaining original IP packet headers for accurate audit trails and flow telemetry.
- **Perimeter Stateful Firewalling**: The Cisco ASA / Firepower Threat Defense (FTD) appliance enforces stateful connection tracking, protocol inspection (HTTP, DNS, SQL*Net, ICMP), and active Snort 3 Intrusion Prevention System (IPS) rule sets to block exploit attempts in real time.

---

## 4. Identity & Access Management (IAM) Architecture

### 4.1 Centralized Identity Provider & SSO
To prevent identity silos across on-premises infrastructure and multiple cloud platforms, authentication is consolidated through a federated **Identity Provider (IdP)** using **Cisco Duo + Cisco Identity Services Engine (ISE)** bridged with **AWS IAM Identity Center** via SAML 2.0 and OpenID Connect (OIDC).

```
   [Faculty / Engineer]
            |
            v
   [Cisco Duo MFA Push]  ---> [Cisco ISE / Azure AD IdP]
                                        | (SAML 2.0 / OIDC Token)
                        +---------------+---------------+
                        |                               |
                        v                               v
            [On-Premises Infrastructure]      [AWS IAM Identity Center]
            (SSH, Console, OpenShift)         (Assumes Temporary Role)
```

### 4.2 Role-Based (RBAC) and Attribute-Based (ABAC) Access Control
Access to cloud and on-premise resources is governed strictly by the **Principle of Least Privilege (PoLP)** and **Attribute-Based Access Control (ABAC)**.

| Stakeholder Role | Permitted Scope & Actions | Enforced Constraints |
| :--- | :--- | :--- |
| **Application Developer** | Read/Write to Dev/Stage EKS namespaces; Read access to application logs; Push access to non-prod ECR registries. | Multi-Factor Authentication (MFA) required; Zero access to production databases or network infrastructure. |
| **Platform Engineer** | Manage Kubernetes cluster resources, CNI configurations, ingress controllers, and Helm charts via GitOps. | Operations must originate from CI/CD pipeline or jumpbox; Production changes require 2-person peer review. |
| **Network Security Admin** | Configure Transit Gateway, Security Groups, Route Tables, VPN tunnels, and Cisco ASA/Firepower policies. | Privileged Session Recording enabled; Mandatory hardware token MFA (FIDO2/WebAuthn). |
| **Remote Faculty Member** | HTTPS access to academic web portals, research repositories, and interactive Jupyter notebook nodes. | Conditional Access: Device posture validation (healthy EDR, OS up to date), contextual IP fencing. |

### 4.3 EKS IAM Roles for Service Accounts (IRSA) & OIDC Federation
A major vulnerability in legacy cloud deployments is embedding static AWS API keys (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`) inside application containers or configmaps. 

This architecture implements **IAM Roles for Service Accounts (IRSA)**:
1. The cloud Kubernetes cluster (EKS) operates as an OIDC Identity Provider recognized by AWS IAM.
2. Microservice pods are associated with a dedicated Kubernetes `ServiceAccount` annotated with an IAM Role ARN: `eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/role-eks-microservice-least-privilege`.
3. The AWS Security Token Service (STS) validates the pod's OIDC JSON Web Token (JWT) and issues temporary, short-lived (1-hour) cryptographic credentials.
4. The IAM policy restricts access specifically to the required S3 research bucket (`s3:GetObject`, `s3:PutObject` on `arn:aws:s3:::cisco-hybrid-academic-research-repo/datasets/*`) and grants permission to decrypt data keys via AWS KMS Customer Managed Keys (CMK).

### 4.4 Privileged Access Management (PAM) & Just-In-Time (JIT) Elevation
- **Zero Standing Privileges**: Engineers do not hold permanent administrator rights.
- **Break-Glass & JIT Workflows**: Administrative access to production infrastructure requires submitting a ticket through ServiceNow/Jira, triggering a time-bounded (e.g., 2-hour) temporary role assumption approved by the Security Lead.
- **Session Auditing**: All privileged terminal sessions (SSH, `kubectl exec`) are audited and recorded via Cisco Secure Workload and AWS CloudTrail.

---

## 5. Cloud Network Segmentation & Security Group Architecture

### 5.1 AWS Transit Gateway Hub-and-Spoke Topology
Rather than using full-mesh VPC peering—which scales poorly ($O(N^2)$ connections) and creates unmanageable routing tables—the cloud network utilizes an **AWS Transit Gateway (TGW)** as a centralized regional hub:
- **Centralized Routing**: Spoke VPCs (Production Workloads, Shared Services, Development) attach to the TGW via dedicated Elastic Network Interfaces (ENIs).
- **Route Table Domain Isolation**: The TGW maintains separate route tables for Production and Non-Production VPCs, preventing development environments from ever routing packets directly into production.
- **Centralized Inspection Capability**: Transit Gateway routing allows insertion of an Inspection Hub VPC containing Cisco Secure Firewall appliances for deep traffic analysis between spokes and on-premise links.

### 5.2 Multi-Tier Subnet Isolation
Within the Production Workload VPC (`172.20.0.0/16`), subnets are segregated into three strict tiers:

```
[Internet / Ingress Traffic]
            |
            v  (Port 443 HTTPS)
+-------------------------------------------------------------+
| TIER 1: Ingress Public Subnet (172.20.1.0/24)               |
| - Application Load Balancer (ALB) with AWS WAF              |
| - sg-prod-ingress-alb                                       |
+-------------------------------------------------------------+
            |
            v  (Port 8080 - Strict SG-to-SG Reference Only)
+-------------------------------------------------------------+
| TIER 2: Application / EKS Worker Subnet (172.20.2.0/24)     |
| - Kubernetes Worker Nodes (Calico CNI, Istio mTLS)          |
| - sg-prod-eks-microservices                                 |
| - Route: 10.10.0.0/16 -> Transit Gateway (Hybrid VPN)       |
+-------------------------------------------------------------+
            |
            v  (Port 5432 - Strict SG-to-SG Reference Only)
+-------------------------------------------------------------+
| TIER 3: Database Isolated Subnet (172.20.3.0/24)            |
| - AWS Aurora / PostgreSQL Managed Database                  |
| - sg-prod-database-isolated                                 |
| - Route: Local VPC ONLY (Zero Internet / Zero Default Route)|
+-------------------------------------------------------------+
```

### 5.3 Stateful Security Groups Matrix (SG-to-SG Referencing)
A critical flaw in standard cloud configurations is using CIDR blocks (e.g., `172.20.2.0/24`) in security group rules. If an unauthorized EC2 instance or rogue container is launched in that subnet, it automatically gains access.

To enforce Zero Trust micro-segmentation, all rules use **Security Group-to-Security Group Referencing (SG ID referencing)**:

| Security Group Name | Ingress Source | Port / Protocol | Egress Destination | Port / Protocol | Purpose / Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `sg-prod-ingress-alb` | `0.0.0.0/0` | TCP / 443 (HTTPS) | `sg-prod-eks-microservices` | TCP / 8080 | Ingress load balancing; forwards validated traffic to microservice pods. |
| `sg-prod-eks-microservices` | `sg-prod-ingress-alb` | TCP / 8080 | `sg-prod-database-isolated` | TCP / 5432 (PostgreSQL) | Application compute tier; handles business logic and DB queries. |
| `sg-prod-eks-microservices` | `10.10.30.0/24` (On-Prem DC) | TCP / 8443 (gRPC/REST) | `10.10.30.50/32` (On-Prem DB) | TCP / 5432 (SQL) | Secure hybrid API integration with on-premise OpenShift and database. |
| `sg-prod-eks-microservices` | `sg-prod-eks-microservices` (Self) | ALL Protocols | `sg-prod-eks-microservices` (Self) | ALL Protocols | EKS inter-pod CNI overlay networking within the node group. |
| `sg-prod-eks-microservices` | `172.16.50.0/24` (Faculty VPN) | TCP / 443 | `sg-prod-vpc-endpoints` | TCP / 443 | Faculty tool access and secure AWS PrivateLink communication. |
| `sg-prod-database-isolated` | `sg-prod-eks-microservices` | TCP / 5432 | **NONE (Deny All)** | **NONE (Deny All)** | Isolated DB tier; allows queries ONLY from app nodes; zero outbound egress. |
| `sg-prod-database-isolated` | `10.10.99.10/32` (Admin Jumpbox)| TCP / 5432 | **NONE (Deny All)** | **NONE (Deny All)** | Controlled DB administration from dedicated on-premise jumpbox. |

### 5.4 Stateless Network Access Control Lists (NACLs)
While Security Groups provide stateful filtering at the hypervisor/ENI layer, Network ACLs provide a **stateless second line of defense** at the subnet boundary:
- Ingress NACL on Tier 3 (Database Subnet) allows inbound traffic only on ports 5432/3306 from Tier 2 CIDR (`172.20.2.0/24`) and ephemeral return ports (`1024-65535`).
- Outbound NACL on Tier 3 strictly forbids any connection to `0.0.0.0/0`, ensuring that even in the catastrophic event of a compromised database process, outbound C2 (Command & Control) callbacks or data exfiltration attempts are blocked at the subnet layer.

---

## 6. Container & Kubernetes Microservice Security (OpenShift / EKS)

### 6.1 Container Network Interface (Calico CNI) Default-Deny Policies
By default, Kubernetes implements a flat network model where any pod can communicate with any other pod across any namespace. In an enterprise hybrid environment, this presents unacceptable lateral movement risk.

Our architecture enforces a **Zero-Trust Default Deny Baseline** using Calico / Cilium CNI:
1. **Global Namespace Lockdown**: A `default-deny-all-traffic` NetworkPolicy is applied across the `production` namespace.
2. **Explicit Whitelisting**: Pod communication is explicitly declared using label selectors:
   - Frontend pods (`tier: web`) accept traffic only from the Ingress Controller.
   - Backend API pods (`tier: application`) accept traffic only from Frontend pods on port 8080 and from the on-premises OpenShift cluster (`10.10.30.0/24`).
   - Database connections are permitted solely from Backend API pods to Tier 3 database endpoints.

### 6.2 Pod Security Standards (PSS) & Runtime Hardening
To prevent container escape attacks and root privilege escalation, the `production` namespace enforces the **Kubernetes Restricted Pod Security Standard**:
- `runAsNonRoot: true`: Containers must run under an unprivileged UID (`10001`).
- `readOnlyRootFilesystem: true`: Container root filesystems are mounted read-only, preventing attackers from downloading tools or malware payloads; temporary files are restricted to memory-backed `emptyDir` mounts (`/tmp`).
- `allowPrivilegeEscalation: false`: Disallows child processes from gaining more privileges than the parent.
- `capabilities.drop: ["ALL"]`: Strips all Linux kernel capabilities (e.g., `CAP_SYS_ADMIN`, `CAP_NET_RAW`).
- `seccompProfile.type: RuntimeDefault`: Enforces default system call filtering.

### 6.3 Istio Service Mesh & Mutual TLS (mTLS 1.3)
All inter-microservice communication is governed by an **Istio Service Mesh**:
- **STRICT Mutual TLS**: Every microservice pod is injected with an Envoy sidecar proxy. All pod-to-pod TCP streams are encrypted using **TLS 1.3** with ephemeral Diffie-Hellman keys.
- **Cryptographic Identity (SPIFFE/SPIRE)**: Services authenticate using cryptographically signed X.509 certificates containing the service identity (e.g., `spiffe://cluster.local/ns/production/sa/academic-frontend-sa`).
- **AuthorizationPolicy RBAC**: Istio enforces method- and path-level HTTP authorization (e.g., Frontend can execute `GET /api/v1/*` but cannot invoke administrative endpoints).

### 6.4 Dynamic Secrets Injection & Image Provenance
- **HashiCorp Vault / AWS Secrets Manager**: Application containers never store database passwords or API keys in configuration files. Secrets are dynamically injected into memory at pod startup via the Kubernetes External Secrets Operator.
- **Container Image Provenance (Cosign & Sigstore)**: Only container images digitally signed by the enterprise CI/CD pipeline are admitted into the cluster. The Kubernetes Admission Controller verifies the cryptographic signature before scheduling any container.

---

## 7. Secure Hybrid Workforce & Remote Faculty Access

### 7.1 Zero Trust Network Access (ZTNA) Architecture
Faculty members requiring access to academic grading tools, HPC compute clusters, and private research data from home or campus connect via a **Zero Trust Network Access (ZTNA)** model powered by **Cisco AnyConnect / Cisco Secure Client**:

```
[Remote Faculty Laptop]
          |
          v  (TLS 1.3 / DTLS Session)
[Cisco AnyConnect Client]  <--->  [Cisco Duo MFA Push Verification]
          |
          v
[Cisco ISE Posture Assessment]
  - OS Patch Level: Compliant
  - Disk Encryption: BitLocker/FileVault Active
  - Cisco Secure Endpoint (EDR): Healthy & Running
          |
          v  (Posture Compliant)
[Cisco ASA / Firepower Perimeter]
  - Assigns Dynamic Dynamic Access Policy (DAP)
  - Allocates IP: 172.16.50.0/24 Pool
  - Grants Access to Authorized Hybrid Services ONLY
```

### 7.2 Cisco Duo Multi-Factor Authentication Integration
- Every remote access request triggers an out-of-band **Cisco Duo Push notification** to the faculty member's registered smartphone or requires a **FIDO2/WebAuthn hardware security key** (e.g., YubiKey).
- Password-only authentication is strictly prohibited, eliminating credential-stuffing and phishing attack vectors.

### 7.3 Cisco ISE Dynamic Posture Assessment
Before granting network access, **Cisco Identity Services Engine (ISE)** executes automated client posture validation:
1. **Operating System Check**: Verifies that Windows/macOS/Linux OS security patches are within 30 days of the latest release.
2. **Endpoint Detection & Response (EDR)**: Checks that Cisco Secure Endpoint / CrowdStrike is active and signatures are current.
3. **Storage Encryption**: Validates that full-disk encryption (BitLocker or FileVault) is enabled.
4. **Quarantine Enforcement**: Non-compliant devices are assigned to an isolated Quarantine VLAN with access limited strictly to software update repositories.

### 7.4 Optimized Split-Tunneling Policy
To prevent bandwidth exhaustion on the enterprise internet uplink from personal streaming or video conferencing traffic:
- **Encrypted Enterprise Tunnel**: Only traffic destined for the enterprise campus (`10.10.0.0/16`), cloud workload VPCs (`172.20.0.0/16`), and internal DNS servers (`10.10.30.50`) is encapsulated in the SSL VPN tunnel.
- **Direct Internet Access**: General internet traffic (e.g., YouTube, Zoom, external web) routes directly through the user's local ISP gateway, optimizing performance while preserving strict security for institutional assets.

---

## 8. Multi-Stakeholder Collaboration & DevSecOps Governance

### 8.1 Stakeholder Responsibility Matrix (RACI)

| Lifecycle Activity | App Developers | Network Designers | K8s Platform Engineers | Security & Compliance |
| :--- | :---: | :---: | :---: | :---: |
| **Application Microservice Code** | **Accountable** | Informed | Consulted | Consulted |
| **VPC, Subnets & Transit Gateway** | Informed | **Accountable** | Consulted | Responsible |
| **Kubernetes Cluster & CNI Policies** | Consulted | Consulted | **Accountable** | Responsible |
| **IAM Policies & Security Groups** | Informed | Responsible | Responsible | **Accountable** |
| **Vulnerability Scanning & SAST** | Responsible | Informed | Responsible | **Accountable** |
| **Production Release Approval** | Consulted | Consulted | Consulted | **Accountable** |

*Legend: **A** = Accountable, **R** = Responsible, **C** = Consulted, **I** = Informed.*

### 8.2 GitOps Infrastructure-as-Code Deployment Workflow
All infrastructure and application configurations are maintained as version-controlled code in Git repositories:
1. **Terraform Repositories**: Manage Transit Gateway, VPCs, Subnets, Route Tables, and AWS Security Groups.
2. **Kubernetes GitOps Repositories**: Manage Calico NetworkPolicies, Istio manifests, and application Helm charts.
3. **ArgoCD Continuous Delivery**: Automatically synchronizes the desired state from Git to both on-premise OpenShift and cloud EKS clusters.

```
[Developer / Engineer] ---> [Git Pull Request] ---> [Automated DevSecOps Pipeline]
                                                              |
                                +-----------------------------+-----------------------------+
                                |                             |                             |
                                v                             v                             v
                         [SAST / Semgrep]             [IaC / Checkov]               [Trivy Container Scan]
                                |                             |                             |
                                +-----------------------------+-----------------------------+
                                                              |
                                                              v  (All Tests Passed)
                                              [Multi-Stakeholder Sign-Off]
                                                              |
                                                              v
                                              [ArgoCD GitOps Production Sync]
```

### 8.3 Automated DevSecOps Pipeline & Security Gates
The CI/CD pipeline enforces four automated security gates before any code reaches production:
1. **Gate 1 (SAST & SCA)**: Semgrep scans application code for OWASP Top 10 vulnerabilities; `pip-audit` / `npm audit` scans libraries.
2. **Gate 2 (IaC Security)**: Checkov and `tfsec` audit Terraform files against the CIS AWS Foundations Benchmark (checking for unencrypted volumes, open 0.0.0.0/0 ingress, missing flow logs).
3. **Gate 3 (Container Image Scanning)**: Aqua Trivy scans built container images; the build fails automatically if any `HIGH` or `CRITICAL` CVEs exist without a patch.
4. **Gate 4 (Cryptographic Image Signing)**: Cosign signs approved container digests, ensuring untampered deployment.

---

## 9. Threat Modeling, Blast Radius Containment & Defense-in-Depth

### 9.1 STRIDE Threat Analysis

| Threat Category | Potential Attack Vector | Applied Architectural Mitigation |
| :--- | :--- | :--- |
| **Spoofing** | Rogue node masquerades as legitimate backend microservice. | Istio STRICT mTLS with SPIFFE X.509 cryptographic identities; 802.1X Dynamic ARP Inspection on switches. |
| **Tampering** | In-flight data tampering over hybrid public interconnect. | IPsec ESP tunnel with SHA-256 HMAC integrity verification and AES-256-GCM authenticated encryption. |
| **Repudiation** | Unauthorized modification of database records or infrastructure. | Immutable AWS CloudTrail logs, Cisco SecureX audit logging, and signed Git commits with GPG. |
| **Information Disclosure** | Data exfiltration from compromised database instance. | Tier 3 Database isolated subnets with zero internet egress; AWS KMS envelope encryption at rest. |
| **Denial of Service** | Volumetric SYN flood or application DDoS targeting academic portals. | AWS Shield Standard + AWS WAF rate-limiting; Cisco ASA Modular Policy Framework (MPF) TCP connection limits. |
| **Elevation of Privilege** | Container breakout or privilege escalation to host node. | Pod Security Standards (Restricted profile: non-root, read-only rootfs, drop ALL capabilities, seccomp). |

### 9.2 Blast Radius Containment & Lateral Movement Mitigation
If an attacker compromises an internet-facing frontend web container:
1. **Container Isolation**: The attacker cannot escalate to root due to the `Restricted` Pod Security Standard.
2. **Filesystem Lockdown**: The read-only root filesystem prevents the execution of downloaded exploit scripts or persistence backdoors.
3. **Network Confinement**: Calico NetworkPolicy drops any outbound packet to arbitrary internet IPs or internal subnets; the container can reach only the backend API on port 8080.
4. **Security Group Quarantine**: At the cloud hypervisor layer, `sg-prod-eks-microservices` permits outbound connections only to the database port and blocks lateral scanning across other VPCs.

### 9.3 Telemetry, Anomaly Detection & Cisco Stealthwatch Integration
Network flow telemetry is continuously exported from Enterprise Core routers (NetFlow v9) and AWS VPC Flow Logs into **Cisco Stealthwatch (Cisco Secure Network Analytics)**:
- **Behavioral Baselining**: Machine learning algorithms establish normal baseline traffic patterns between on-premise OpenShift and cloud EKS workloads.
- **Anomaly Detection**: Flags sudden spikes in data volume (potential exfiltration), port scanning, or unexpected connection attempts to restricted database ports.
- **Automated Mitigation**: Stealthwatch triggers automated quarantine via Cisco ISE and AWS Security Group dynamic updates to sever malicious connections instantly.

### 9.4 Centralized SIEM & Cisco SecureX Visibility
Security alerts from Cisco ASA/Firepower, Cisco Duo, AWS GuardDuty, and Kubernetes Audit Logs aggregate into **Cisco SecureX** and a centralized SIEM (Splunk / Elastic):
- Unified single-pane-of-glass dashboard for the Security Operations Center (SOC).
- Automated Incident Response Playbooks (SOAR) to isolate compromised endpoints within seconds.

---

## 10. Engineering Evaluation: Simplicity, Security & Scalability

A fundamental challenge in enterprise architecture is avoiding solutions that are so complex they overwhelm administrators or degrade application performance. The table below evaluates how our architecture balances these competing priorities:

| Architecture Dimension | Simplicity Engineering | Security Rigor | Scalability Mechanism |
| :--- | :--- | :--- | :--- |
| **Network Interconnect** | Single logical Transit Gateway hub replaces complex $N^2$ VPC mesh; standardized BGP routing. | High-grade IPsec IKEv2 AES-256 encryption; perimeter DPI via Cisco Firepower. | TGW supports up to 50 Gbps throughput per VPC attachment and scales to 5,000 VPCs. |
| **Identity & IAM** | Single Sign-On (SSO) with unified identity provider; zero static cloud API keys. | OIDC temporary token federation (IRSA); context-aware Duo MFA and ISE posture checks. | Centralized IAM scales effortlessly to thousands of faculty members and microservices. |
| **Segmentation** | Reusable Security Group referencing rules instead of fragile, high-maintenance IP CIDR lists. | Micro-segmented 3-tier subnets; zero-egress database isolation; Calico default-deny. | New microservice pods automatically inherit security group and NetworkPolicy rules upon deployment. |
| **Workforce Access** | Optimized split-tunneling allows faculty seamless, one-click AnyConnect access from anywhere. | Continuous endpoint posture validation; automated quarantine of non-compliant laptops. | Elastic cloud gateways and dynamic VPN pools scale with peak academic registration periods. |
| **DevSecOps Governance** | Declarative GitOps (ArgoCD) automates infrastructure provisioning without manual intervention. | Automated multi-stage security gates (SAST, SCA, Checkov, Trivy, Cosign image signing). | Reusable CI/CD templates support rapid onboarding of new academic research applications. |

---

## 11. Cisco Packet Tracer Implementation & CLI Verification Guide

The accompanying Cisco Packet Tracer simulation implements this exact architecture. Below is the CLI verification reference for network validation:

### 11.1 Key Device Roles & Hostnames

| Packet Tracer Device | Model / Type | Config File Reference |
| :--- | :--- | :--- |
| **ENT-CORE-RTR-01** | Cisco 2911 / 4331 ISR | `packet_tracer_configs/01_Enterprise_Core_Router.ios` |
| **ENT-PERIMETER-FW-01** | Cisco ASA 5506-X Firewall | `packet_tracer_configs/02_Enterprise_Firewall_ASA.cfg` |
| **ENT-DC-SW-01** | Cisco Catalyst 2960 / 3650 | `packet_tracer_configs/03_Enterprise_DC_Switch.ios` |
| **ISP-BACKBONE-RTR** | Cisco 2911 ISR | `packet_tracer_configs/04_ISP_Internet_Router.ios` |
| **CLOUD-TRANSIT-GW-01** | Cisco 2911 / CSR1000v | `packet_tracer_configs/05_Cloud_Gateway_Router.ios` |
| **CLOUD-VPC-SW-01** | Cisco Catalyst 2960 | `packet_tracer_configs/06_Cloud_Workload_Switch.ios` |

### 11.2 Step-by-Step Verification Commands

#### A. Verify Layer 2 Switch Hardening (ENT-DC-SW-01)
```ios
ENT-DC-SW-01# show vlan brief
ENT-DC-SW-01# show interfaces trunk
ENT-DC-SW-01# show port-security
ENT-DC-SW-01# show ip dhcp snooping
ENT-DC-SW-01# show ip arp inspection
```

#### B. Verify Core Routing & OSPF (ENT-CORE-RTR-01)
```ios
ENT-CORE-RTR-01# show ip route
ENT-CORE-RTR-01# show ip ospf neighbor
ENT-CORE-RTR-01# show ip interface brief
```

#### C. Verify Cisco ASA Firewall & IPsec VPN (ENT-PERIMETER-FW-01)
```cisco-asa
ENT-PERIMETER-FW-01# show nameif
ENT-PERIMETER-FW-01# show access-list
ENT-PERIMETER-FW-01# show nat
ENT-PERIMETER-FW-01# show crypto ikev2 sa
ENT-PERIMETER-FW-01# show crypto ipsec sa
ENT-PERIMETER-FW-01# show vpn-sessiondb anyconnect
```

#### D. Verify Cloud Transit Gateway & Security Rules (CLOUD-TRANSIT-GW-01)
```ios
CLOUD-TRANSIT-GW-01# show crypto isakmp sa
CLOUD-TRANSIT-GW-01# show crypto ipsec sa
CLOUD-TRANSIT-GW-01# show ip access-lists
CLOUD-TRANSIT-GW-01# show ip route
```

#### E. End-to-End Connectivity & Security Validation Tests
1. **Faculty to Cloud Microservices**: Ping / HTTP request from Faculty PC (`10.10.10.10`) to Cloud Microservice (`172.20.2.10`) -> **SUCCESS** (traverses encrypted IPsec VPN).
2. **Staff/Student LAN to Database Isolation**: Attempt connection from Student PC (`10.10.20.10`) to Database (`172.20.3.10` or `10.10.30.50`) -> **DROPPED BY ACL** (segregation verified).
3. **Direct Cloud Database Ingress from Internet**: Attempt connection from Public Internet PC (`209.165.200.10`) to Cloud DB (`172.20.3.10`) -> **BLOCKED** (no route / dropped by security group).
4. **On-Premises DMZ Isolation**: Attempt connection from DMZ Web Server (`192.168.50.10`) to Enterprise Internal LAN (`10.10.10.0/24`) -> **DROPPED BY ASA ACL**.

---

## 12. Conclusion & Future Roadmap

This capstone project presents a production-grade, highly resilient cybersecurity architecture for enterprise hybrid data centers and multi-cloud workloads. By combining the strengths of Cisco enterprise networking technologies with modern cloud-native security paradigms:
- The private data center remains fortified behind Cisco ASA/Firepower inspection and Layer 2 switch hardening.
- Cloud workloads in AWS EKS operate under Zero-Trust micro-segmentation with SG-to-SG referencing, Calico CNI default-deny, and Istio mTLS.
- Identity is unified through OIDC federation and Cisco Duo MFA, completely removing static credentials.
- Faculty members enjoy uninterrupted, secure access from any location via Cisco AnyConnect ZTNA with continuous posture checks.
- Multi-stakeholder DevSecOps pipelines guarantee that security is continuously validated at every stage of the software delivery lifecycle.

### Future Roadmap & Enhancements
1. **eBPF Deep Observability**: Upgrade Kubernetes network security to Cilium eBPF for Layer 7 socket-level observability and acceleration.
2. **AI-Driven Threat Hunting**: Integrate Cisco Talos threat intelligence feeds with automated SOAR playbooks for predictive zero-day exploit neutralization.
3. **Multi-Region Disaster Recovery**: Extend AWS Transit Gateway Peering to a secondary geographic region with automated DNS failover via Amazon Route 53.

---
**Report Compiled for Cisco Virtual Internship 2026 Submission**  
*Project Artifacts: Packet Tracer Configs (`.ios`/`.cfg`), Terraform IaC (`.tf`), Kubernetes Manifests (`.yaml`), DevSecOps Pipeline (`.yml`).*
