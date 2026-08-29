# CISCO PACKET TRACER STEP-BY-STEP LAB BUILD & SIMULATION GUIDE

**Project**: Secure Hybrid Data Center Network Architecture  
**Simulation Platform**: Cisco Packet Tracer v8.2+  
**Target Submission**: Packet Tracer Simulation & CLI Configs  

---

## 1. Required Devices in Packet Tracer Workspace

| Topology Role | Recommended Packet Tracer Device | Workspace Label / Hostname |
| :--- | :--- | :--- |
| **Enterprise Core Router** | Cisco 2911 or 4331 Router | `ENT-CORE-RTR-01` |
| **Enterprise Perimeter Firewall** | Cisco ASA 5506-X Security Appliance | `ENT-PERIMETER-FW-01` |
| **Enterprise Data Center Switch** | Cisco Catalyst 2960 or 3650 Switch | `ENT-DC-SW-01` |
| **ISP WAN Backbone Router** | Cisco 2911 Router | `ISP-BACKBONE-RTR` |
| **Cloud Transit Gateway Router** | Cisco 2911 or 4331 Router | `CLOUD-TRANSIT-GW-01` |
| **Cloud VPC Workload Switch** | Cisco Catalyst 2960 Switch | `CLOUD-VPC-SW-01` |
| **Faculty Workstation (LAN)** | PC / Laptop | `Faculty-PC-01` (`10.10.10.10`) |
| **Student / Staff PC** | PC / Laptop | `Student-PC-01` (`10.10.20.10`) |
| **On-Prem OpenShift Server** | Server-PT | `OpenShift-Master` (`10.10.30.10`) |
| **On-Prem Database Server** | Server-PT | `OnPrem-DB-Server` (`10.10.30.50`) |
| **DMZ Web Server** | Server-PT | `DMZ-Web-Server` (`192.168.50.10`) |
| **Public Internet Web/DNS Server**| Server-PT | `Public-NetAcad-Server` (`209.165.200.225`)|
| **Cloud EKS Worker Pod** | Server-PT | `Cloud-EKS-Pod-01` (`172.20.2.10`) |
| **Cloud Managed RDS Database** | Server-PT | `Cloud-Aurora-DB` (`172.20.3.10`) |

---

## 2. Physical Cabling & Port Interconnects

### A. Enterprise On-Premises Interconnects
1. Connect `ENT-CORE-RTR-01` `Gig0/0` <---> `ENT-DC-SW-01` `Gig0/1` (Copper Straight-Through - 802.1Q Trunk)
2. Connect `ENT-CORE-RTR-01` `Gig0/1` <---> `ENT-PERIMETER-FW-01` `Gig1/1 (inside)` (Copper Straight-Through)
3. Connect `ENT-PERIMETER-FW-01` `Gig1/2 (dmz)` <---> `DMZ-Web-Server` `FastEthernet0` (Copper Straight-Through)
4. Connect `ENT-DC-SW-01` `FastEthernet0/1` <---> `Faculty-PC-01` (VLAN 10)
5. Connect `ENT-DC-SW-01` `FastEthernet0/6` <---> `Student-PC-01` (VLAN 20)
6. Connect `ENT-DC-SW-01` `FastEthernet0/11` <---> `OpenShift-Master` (VLAN 30)
7. Connect `ENT-DC-SW-01` `FastEthernet0/12` <---> `OnPrem-DB-Server` (VLAN 30)

### B. ISP & WAN Interconnects
1. Connect `ENT-PERIMETER-FW-01` `Gig1/3 (outside)` <---> `ISP-BACKBONE-RTR` `Gig0/0` (Copper Straight-Through)
2. Connect `ISP-BACKBONE-RTR` `Gig0/1` <---> `CLOUD-TRANSIT-GW-01` `Gig0/0` (Copper Straight-Through)
3. Connect `ISP-BACKBONE-RTR` `Gig0/2` <---> `Public-NetAcad-Server` `FastEthernet0` (Copper Straight-Through)

### C. Cloud VPC Interconnects
1. Connect `CLOUD-TRANSIT-GW-01` `Gig0/1` <---> `CLOUD-VPC-SW-01` `Gig0/1` (Copper Straight-Through - 802.1Q Trunk)
2. Connect `CLOUD-VPC-SW-01` `FastEthernet0/2` <---> `Cloud-EKS-Pod-01` (VLAN 20)
3. Connect `CLOUD-VPC-SW-01` `FastEthernet0/3` <---> `Cloud-Aurora-DB` (VLAN 30)

---

## 3. Step-by-Step Configuration Deployment

To configure each device, open the device in Cisco Packet Tracer, click on the **CLI** tab, press Enter, and paste the corresponding script located in the `packet_tracer_configs/` folder:

1. **Step 1**: Configure `ISP-BACKBONE-RTR` using `packet_tracer_configs/04_ISP_Internet_Router.ios`
2. **Step 2**: Configure `ENT-DC-SW-01` using `packet_tracer_configs/03_Enterprise_DC_Switch.ios`
3. **Step 3**: Configure `ENT-CORE-RTR-01` using `packet_tracer_configs/01_Enterprise_Core_Router.ios`
4. **Step 4**: Configure `ENT-PERIMETER-FW-01` using `packet_tracer_configs/02_Enterprise_Firewall_ASA.cfg`
5. **Step 5**: Configure `CLOUD-VPC-SW-01` using `packet_tracer_configs/06_Cloud_Workload_Switch.ios`
6. **Step 6**: Configure `CLOUD-TRANSIT-GW-01` using `packet_tracer_configs/05_Cloud_Gateway_Router.ios`

---

## 4. Endpoint IP Configurations

Configure the Static / DHCP IP settings on the endpoints:

- **Faculty-PC-01**:
  - IP Address: `10.10.10.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.10.10.1`
  - DNS Server: `10.10.30.50`

- **Student-PC-01**:
  - IP Address: `10.10.20.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.10.20.1`

- **OpenShift-Master (Server)**:
  - IP Address: `10.10.30.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.10.30.1`

- **OnPrem-DB-Server (Server)**:
  - IP Address: `10.10.30.50`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.10.30.1`

- **DMZ-Web-Server (Server)**:
  - IP Address: `192.168.50.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `192.168.50.1`

- **Public-NetAcad-Server (Server)**:
  - IP Address: `209.165.200.225`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `209.165.200.1`

- **Cloud-EKS-Pod-01 (Server)**:
  - IP Address: `172.20.2.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `172.20.2.1`

- **Cloud-Aurora-DB (Server)**:
  - IP Address: `172.20.3.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `172.20.3.1`

---

## 5. Verification & Security Testing Scenarios

Open the Command Prompt on the respective PCs/Servers in Packet Tracer and run the following tests:

| Test Case | Source Device | Target Destination | Expected Result | Security Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Test 1: Hybrid VPN Tunnel** | `Faculty-PC-01` | Ping `172.20.2.10` (Cloud EKS) | **Reply Received (100% Success)** | IPsec VPN securely bridges on-prem faculty to cloud microservices |
| **Test 2: Student LAN Segregation** | `Student-PC-01` | Ping `10.10.30.50` (On-Prem DB) | **Request Timed Out (Blocked)** | ACL-CAMPUS-RESTRICTIONS prevents unauthorized database probing |
| **Test 3: Cloud DB Isolation** | `Public-NetAcad-Server` | Ping `172.20.3.10` (Cloud DB) | **Request Timed Out (Blocked)** | Cloud Database subnet has zero public ingress/egress routes |
| **Test 4: Cloud App to DB** | `Cloud-EKS-Pod-01` | Ping `172.20.3.10` (Cloud DB) | **Reply Received (100% Success)** | Microservices tier is authorized to communicate with DB tier |
| **Test 5: DMZ Inbound Security** | `DMZ-Web-Server` | Ping `10.10.10.10` (Faculty PC) | **Request Timed Out (Blocked)** | ASA DMZ ACL blocks DMZ servers from initiating sessions inside |

---
*Save your completed Packet Tracer file as `Name-CollegeName-CyberSecurity.pkt` for submission.*
