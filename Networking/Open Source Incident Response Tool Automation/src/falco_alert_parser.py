import argparse
import re
import os

def parse_falco_log(path):
    if not os.path.exists(path):
        print(f"[!] File not found: {path}")
        return

    with open(path, 'r') as f:
        for line in f:
            # Look for lines with alert-level info
            if "Priority: " in line and "Rule:" in line:
                # Extract structured fields from real Falco alert line
                timestamp = line.split(': ')[0]
                rule = re.search(r'Rule: (.*?) \(', line)
                priority = re.search(r'Priority: (\w+)', line)

                if rule and priority:
                    print(f"[{priority.group(1)}] {timestamp} - Rule Triggered: {rule.group(1)}")
                    details = line.split('(')[-1].strip(')\n')
                    print(f"    → Details: {details}")

def main():
    parser = argparse.ArgumentParser(description="Falco Log Parser")
    parser.add_argument("-l", "--log", required=True, help="Path to /var/log/falco.log")
    args = parser.parse_args()
    parse_falco_log(args.log)

if __name__ == "__main__":
    main()
