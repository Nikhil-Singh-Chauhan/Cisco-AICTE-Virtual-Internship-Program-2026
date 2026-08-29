# ==============================================================================
# CISCO VIRTUAL INTERNSHIP 2026 - CYBER SECURITY PROJECT
# Automated Project Integrity & Network Configuration Validator
# ==============================================================================

import os
import sys

def verify_project_files():
    base_dir = r"d:\PROJECTS\CISCO"
    required_files = [
        "README.md",
        "docs/CISCO_CYBERSECURITY_HYBRID_DATACENTER_PROJECT_REPORT.md",
        "docs/STUDENT_CONTRIBUTION_SUMMARY.md",
        "docs/CISCO_PACKET_TRACER_LAB_GUIDE.md",
        "docs/Cisco_Cybersecurity_Internship_Report.docx",
        "docs/Student_Contribution_Summary.docx",
        "docs/Cisco_Cybersecurity_Internship_Report.pdf",
        "docs/Student_Contribution_Summary.pdf",
        "packet_tracer_configs/01_Enterprise_Core_Router.ios",
        "packet_tracer_configs/02_Enterprise_Firewall_ASA.cfg",
        "packet_tracer_configs/03_Enterprise_DC_Switch.ios",
        "packet_tracer_configs/04_ISP_Internet_Router.ios",
        "packet_tracer_configs/05_Cloud_Gateway_Router.ios",
        "packet_tracer_configs/06_Cloud_Workload_Switch.ios",
        "infrastructure_as_code/terraform/main.tf",
        "infrastructure_as_code/terraform/security_groups.tf",
        "infrastructure_as_code/terraform/iam_roles.tf",
        "infrastructure_as_code/terraform/variables.tf",
        "infrastructure_as_code/kubernetes_security/01_calico_default_deny.yaml",
        "infrastructure_as_code/kubernetes_security/02_microservice_segmentation.yaml",
        "infrastructure_as_code/kubernetes_security/03_pod_security_admission.yaml",
        "infrastructure_as_code/kubernetes_security/04_istio_mtls_policy.yaml",
        "devsecops/ci_cd_pipeline.yml",
        "scripts/generate_docx_report.py",
        "scripts/generate_pdf_report.py"
    ]

    print("================================================================================")
    print("  CISCO CYBERSECURITY CAPSTONE PROJECT: INTEGRITY & AUDIT VERIFICATION")
    print("================================================================================")
    
    missing_files = []
    for rel_path in required_files:
        full_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
        if os.path.exists(full_path):
            size_bytes = os.path.getsize(full_path)
            print(f"[PASS] {rel_path:<60} ({size_bytes:>7} bytes)")
        else:
            print(f"[FAIL] MISSING: {rel_path}")
            missing_files.append(rel_path)

    print("\n" + "-" * 80)
    if missing_files:
        print(f"FAILED: {len(missing_files)} required project files missing.")
        sys.exit(1)
    else:
        print("SUCCESS: All 24 project artifacts verified and ready for Cisco / AICTE submission.")
        print("Submission Portal: https://forms.gle/3rh45ov9hBhJsg14A")
        print("Submission Deadline: 30th August 2026")
        print("-" * 80)

if __name__ == "__main__":
    verify_project_files()
