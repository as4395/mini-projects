import argparse
import json

def parse_log_line(line):
    # Attempts to parse a single log line as JSON.
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None

def parse_log_file(log_path):
    # Reads and analyzes Cowrie honeypot log entries.
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = parse_log_line(line)
            if not entry:
                continue

            event = entry.get('eventid', '')
            ip = entry.get('src_ip')

            # Detect failed login attempts
            if event == 'cowrie.login.failed':
                print(f"[!] Failed login: User='{entry.get('username')}', IP={ip}")

            # Detect successful logins
            elif event == 'cowrie.login.success':
                print(f"[+] Successful login: User='{entry.get('username')}', IP={ip}")

            # Show attacker commands
            elif event == 'cowrie.command.input':
                print(f"[*] Command from {ip}: {entry.get('input')}")

            # Show SSH client fingerprint
            elif event == 'cowrie.client.version':
                print(f"[*] Client version: {entry.get('version')}, IP={ip}")

def parse_args():
    # Parses CLI arguments.
    parser = argparse.ArgumentParser(description="Cowrie Honeypot Log Parser")
    parser.add_argument("-l", "--logfile", required=True, help="Path to Cowrie combined.log file")
    return parser.parse_args()

def main():
    args = parse_args()
    parse_log_file(args.logfile)

if __name__ == "__main__":
    main()
