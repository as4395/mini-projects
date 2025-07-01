import re
import argparse

def scan_for_static_issues(file_path):
    issues = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            if "eval(" in line or "exec(" in line:
                issues.append((i, "Use of dangerous function"))
            if re.search(r'password\s*=\s*["\'].*["\']', line, re.IGNORECASE):
                issues.append((i, "Hardcoded password"))
            if "import os" in line or "import subprocess" in line:
                issues.append((i, "Use of system-level imports"))
    return issues

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static Code Analyzer")
    parser.add_argument("--file", required=True, help="Path to Python file to analyze")
    args = parser.parse_args()

    findings = scan_for_static_issues(args.file)
    print("[*] Static Analysis Report:")
    for line_no, issue in findings:
        print(f"Line {line_no}: {issue}")
