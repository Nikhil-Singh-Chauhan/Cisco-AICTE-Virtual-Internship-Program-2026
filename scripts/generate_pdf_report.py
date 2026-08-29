# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Automated Report Generator: Python to PDF Generator (.pdf)
# Fix: Python 3.8 Windows hashlib.md5 compatibility patch
# ==============================================================================

import hashlib
_orig_md5 = hashlib.md5
def _safe_md5(*args, **kwargs):
    kwargs.pop('usedforsecurity', None)
    return _orig_md5(*args, **kwargs)
hashlib.md5 = _safe_md5

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        self.setStrokeColor(colors.HexColor("#005073"))
        self.setLineWidth(0.5)
        # Header
        self.line(40, letter[1] - 40, letter[0] - 40, letter[1] - 40)
        self.drawString(40, letter[1] - 35, "Cisco Virtual Internship 2026 | Cyber Security Capstone Project")
        # Footer
        self.line(40, 45, letter[0] - 40, 45)
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 40, 32, page_text)
        self.drawString(40, 32, "Confidential - Submitted to Cisco & AICTE NetAcad Review Portal")
        self.restoreState()

def build_pdf(filename, title_text, elements_generator):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=55,
        bottomMargin=55
    )
    styles = getSampleStyleSheet()
    story = elements_generator(styles)
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF: {filename}")

def get_report_story(styles):
    story = []

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#005073'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1B365D'),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#005073'),
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    story.append(Paragraph("CISCO VIRTUAL INTERNSHIP 2026", title_style))
    story.append(Paragraph("Secure Hybrid Data Center Network Architecture & Multi-Cloud Workload Protection", subtitle_style))

    # Metadata Table
    meta_data = [
        [Paragraph("<b>Program & Authority:</b>", body_style), Paragraph("Cisco Virtual Internship 2026 / AICTE & Cisco Networking Academy", body_style)],
        [Paragraph("<b>Problem Statement:</b>", body_style), Paragraph("Cyber Security: Enterprise Hybrid Data Center & Workload Security", body_style)],
        [Paragraph("<b>Key Technologies:</b>", body_style), Paragraph("Cisco ASA/Firepower, Cisco ISE, Cisco Duo, AWS TGW, Calico CNI, Istio mTLS", body_style)],
        [Paragraph("<b>Submission Deadline:</b>", body_style), Paragraph("30th August 2026", body_style)],
    ]
    meta_table = Table(meta_data, colWidths=[150, 380])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F8FA')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#B0C8D6')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D5E3EC')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Modern enterprise and higher education institutions are transitioning from isolated on-premises "
        "data centers to distributed hybrid multi-cloud architectures. Today's academic and enterprise "
        "workloads span private data centers (Red Hat OpenShift, local database clusters) and public cloud "
        "environments (AWS EKS, RDS, Azure AKS). While this hybrid paradigm unlocks unprecedented scalability "
        "and collaborative power, it fundamentally dissolves the traditional network perimeter.",
        body_style
    ))
    story.append(Paragraph(
        "This project presents an enterprise-grade Secure Hybrid Data Center Network Architecture designed to "
        "balance simplicity, rock-solid security, and linear scalability. Leveraging Cisco enterprise security "
        "solutions (Cisco ASA 5506-X / Firepower, Cisco ISE, Cisco Duo MFA, Cisco Stealthwatch) combined with "
        "cloud-native controls (AWS Transit Gateway, SG-to-SG referencing, Calico CNI default-deny, and Istio mTLS), "
        "this architecture guarantees that any breach within a single container, virtual machine, or remote endpoint "
        "is immediately contained, logged, and isolated.",
        body_style
    ))

    # 2. Key Objectives & Threat Vectors
    story.append(Paragraph("2. Core Technical Objectives", h1_style))
    story.append(Paragraph("• <b>Hybrid Interconnect Protection:</b> Secure site-to-site IPsec VPN over BGP with IKEv2 / AES-256-GCM and Cisco ASA stateful deep inspection.", bullet_style))
    story.append(Paragraph("• <b>Unified Identity & Access Management (IAM):</b> Eliminate static credentials via OIDC federation (EKS IRSA) and Least-Privilege RBAC.", bullet_style))
    story.append(Paragraph("• <b>Multi-VPC Micro-Segmentation:</b> Hub-and-Spoke Transit Gateway topology with 3-tier subnets and SG-to-SG referencing.", bullet_style))
    story.append(Paragraph("• <b>Kubernetes & Microservice Hardening:</b> Calico CNI default-deny network policies, Restricted Pod Security Standards, and Istio mTLS 1.3.", bullet_style))
    story.append(Paragraph("• <b>Secure Remote Faculty Access (ZTNA):</b> Cisco AnyConnect SSL VPN with Cisco Duo MFA and dynamic Cisco ISE posture validation.", bullet_style))
    story.append(Paragraph("• <b>DevSecOps Governance:</b> Automated CI/CD security gates (SAST, Checkov IaC, Trivy container scanning, Cosign signing).", bullet_style))

    # 3. IP Addressing Matrix
    story.append(Paragraph("3. Network Topology & IP Addressing Allocation", h1_style))
    ip_table_data = [
        [Paragraph("<b>Segment Name</b>", body_style), Paragraph("<b>Subnet CIDR</b>", body_style), Paragraph("<b>VLAN / Zone</b>", body_style), Paragraph("<b>Security Function</b>", body_style)],
        [Paragraph("Enterprise Core Transit", body_style), Paragraph("10.10.0.0/30", body_style), Paragraph("P2P", body_style), Paragraph("Core Router to ASA Inside link", body_style)],
        [Paragraph("Faculty Workstations", body_style), Paragraph("10.10.10.0/24", body_style), Paragraph("VLAN 10", body_style), Paragraph("On-Premises Faculty Desktops (802.1X)", body_style)],
        [Paragraph("Student & Staff LAN", body_style), Paragraph("10.10.20.0/24", body_style), Paragraph("VLAN 20", body_style), Paragraph("General Campus; DB access blocked", body_style)],
        [Paragraph("On-Premises OpenShift/DC", body_style), Paragraph("10.10.30.0/24", body_style), Paragraph("VLAN 30", body_style), Paragraph("Private DC nodes & DB servers", body_style)],
        [Paragraph("Network Management", body_style), Paragraph("10.10.99.0/24", body_style), Paragraph("VLAN 99", body_style), Paragraph("Admin jumpboxes & out-of-band SSH", body_style)],
        [Paragraph("Faculty AnyConnect Pool", body_style), Paragraph("172.16.50.0/24", body_style), Paragraph("SSL VPN", body_style), Paragraph("Dynamic IP pool for remote ZTNA faculty", body_style)],
        [Paragraph("Enterprise WAN Edge", body_style), Paragraph("203.0.113.0/30", body_style), Paragraph("Outside (0)", body_style), Paragraph("Cisco ASA Public IP (203.0.113.2)", body_style)],
        [Paragraph("Cloud Transit WAN Edge", body_style), Paragraph("198.51.100.0/30", body_style), Paragraph("Cloud WAN", body_style), Paragraph("Cloud Transit Gateway (198.51.100.2)", body_style)],
        [Paragraph("Cloud Tier 1 (ALB Ingress)", body_style), Paragraph("172.20.1.0/24", body_style), Paragraph("Public", body_style), Paragraph("AWS Application Load Balancers & WAF", body_style)],
        [Paragraph("Cloud Tier 2 (EKS App)", body_style), Paragraph("172.20.2.0/24", body_style), Paragraph("Private", body_style), Paragraph("Kubernetes workers; zero public IPs", body_style)],
        [Paragraph("Cloud Tier 3 (Isolated DB)", body_style), Paragraph("172.20.3.0/24", body_style), Paragraph("Isolated", body_style), Paragraph("Managed DB (RDS); zero internet routing", body_style)],
    ]
    t = Table(ip_table_data, colWidths=[120, 85, 75, 250])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#005073')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#B0C8D6')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E0E0E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # 4. Cloud Micro-segmentation & IAM
    story.append(Paragraph("4. Cloud Security Groups & IAM Architecture", h1_style))
    story.append(Paragraph(
        "<b>Stateful Security Groups (SG-to-SG Referencing):</b> Rather than relying on fragile CIDR blocks, "
        "cloud security groups reference peer Security Group IDs. Ingress to the EKS microservices tier is permitted "
        "strictly from <code>sg-prod-ingress-alb</code> on port 8080. Database ingress is strictly permitted ONLY from "
        "<code>sg-prod-eks-microservices</code> on port 5432, preventing rogue instances or compromised containers in "
        "other subnets from probing the persistence layer.",
        body_style
    ))
    story.append(Paragraph(
        "<b>IAM Roles for Service Accounts (IRSA):</b> Pods running in AWS EKS assume temporary, scoped IAM roles "
        "via OIDC Web Identity Federation. Applications never store static access keys, eliminating secret leakage risks.",
        body_style
    ))

    # 5. Kubernetes & Remote Access
    story.append(Paragraph("5. Kubernetes & Remote Faculty Access Security", h1_style))
    story.append(Paragraph("• <b>Calico CNI Default-Deny:</b> Global default-deny network policies enforce zero-trust pod communication.", bullet_style))
    story.append(Paragraph("• <b>Istio mTLS 1.3:</b> Mutual TLS with cryptographic SPIFFE identities for all pod-to-pod streams.", bullet_style))
    story.append(Paragraph("• <b>Pod Security Standards:</b> Restricted profile (non-root execution, read-only root filesystems, drop all capabilities).", bullet_style))
    story.append(Paragraph("• <b>Cisco AnyConnect ZTNA:</b> Remote faculty access protected by Cisco Duo MFA push notifications and Cisco ISE dynamic endpoint posture checks (OS patch, disk encryption, EDR health).", bullet_style))

    # 6. Evaluation & Summary
    story.append(Paragraph("6. Architectural Balance: Simplicity, Security & Scale", h1_style))
    story.append(Paragraph(
        "The architecture successfully balances operational simplicity (Transit Gateway hub, GitOps automation, unified SSO), "
        "uncompromising security (defense-in-depth, zero-trust micro-segmentation, continuous telemetry with Cisco Stealthwatch), "
        "and cloud-scale elasticity (supporting thousands of microservices and up to 50 Gbps per VPC attachment).",
        body_style
    ))

    return story

def get_student_summary_story(styles):
    story = []
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#005073'),
        alignment=1,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1B365D'),
        alignment=1,
        spaceAfter=12
    )
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#005073'),
        spaceBefore=10,
        spaceAfter=5
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=5
    )
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    story.append(Paragraph("CISCO VIRTUAL INTERNSHIP 2026", title_style))
    story.append(Paragraph("Individual Project Contribution Summary Document", subtitle_style))

    student_meta = [
        [Paragraph("<b>Candidate Name:</b>", body_style), Paragraph("[Your Full Name]", body_style)],
        [Paragraph("<b>AICTE Registration ID:</b>", body_style), Paragraph("[Your AICTE ID]", body_style)],
        [Paragraph("<b>College Name:</b>", body_style), Paragraph("[Your College Name / GLBITM]", body_style)],
        [Paragraph("<b>Technology Track:</b>", body_style), Paragraph("Cyber Security & Enterprise Networking", body_style)],
        [Paragraph("<b>Project Title:</b>", body_style), Paragraph("Secure Hybrid Data Center Network Architecture", body_style)],
    ]
    t = Table(student_meta, colWidths=[150, 380])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F8FA')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#B0C8D6')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D5E3EC')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    story.append(Paragraph("1. Individual Contribution Breakdown", h1_style))
    story.append(Paragraph("• <b>Hybrid IPsec VPN & Edge Firewall:</b> Configured Site-to-Site IKEv2 IPsec VPN (AES-256-GCM / SHA-256 / DH 14) and Identity NAT on Cisco ASA 5506-X to seamlessly connect on-premise OpenShift clusters to AWS Transit Gateway.", bullet_style))
    story.append(Paragraph("• <b>Cloud VPC Segmentation & Security Groups:</b> Authored Terraform code for 3-tier subnets and SG-to-SG referencing rules, ensuring complete isolation of database tiers from public ingress.", bullet_style))
    story.append(Paragraph("• <b>Kubernetes Microservice Security:</b> Created Calico default-deny NetworkPolicies, Restricted Pod Security Standards, and Istio STRICT mTLS 1.3 manifests.", bullet_style))
    story.append(Paragraph("• <b>Zero-Trust Remote Faculty Access:</b> Designed Cisco AnyConnect SSL VPN profiles with Cisco Duo MFA push notifications and Cisco ISE posture compliance assessment.", bullet_style))
    story.append(Paragraph("• <b>DevSecOps Pipeline Automation:</b> Integrated Semgrep SAST, Checkov IaC scanning, and Trivy container scanning into automated CI/CD security gates.", bullet_style))
    story.append(Paragraph("• <b>Packet Tracer Lab Simulation:</b> Built and validated the entire multi-device network topology with complete CLI configuration scripts.", bullet_style))

    story.append(Paragraph("2. Cisco Packet Tracer Deliverables", h1_style))
    story.append(Paragraph("The submission includes tested configuration files for Enterprise Core Router, ASA Perimeter Firewall, Data Center Switch, ISP Router, Cloud Transit Gateway Router, and Cloud Workload Switch.", body_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Declaration:</b> I hereby declare that this project work is original and completed in accordance with Cisco Networking Academy and AICTE guidelines.", body_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Candidate Signature: _______________________          Date: 24th August 2026", body_style))

    return story

def main():
    pdf_report_path = r"d:\PROJECTS\CISCO\docs\Cisco_Cybersecurity_Internship_Report.pdf"
    pdf_summary_path = r"d:\PROJECTS\CISCO\docs\Student_Contribution_Summary.pdf"

    build_pdf(pdf_report_path, "Cisco Cybersecurity Project Report", get_report_story)
    build_pdf(pdf_summary_path, "Student Contribution Summary", get_student_summary_story)

if __name__ == "__main__":
    main()
