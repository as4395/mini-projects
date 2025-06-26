# Open Source Incident Response Tool Automation (Falco)

This project sets up the open-source runtime threat detection tool **Falco**, automates its installation on a Linux host, and includes a Python-based log parser to scan Falco alerts for potential security incidents.

## Features

- Installs Falco on a Linux system (Ubuntu/Debian)
- Starts the Falco daemon to detect suspicious activity (e.g., shell spawning, file changes, privilege abuse)
- Includes a log parser to extract and categorize security alerts from `/var/log/falco.log`
- Helps simulate real-world SIEM alert triage in homelab environments

## Usage

### 1. Install Falco

```bash
sudo python3 src/setup_falco.py
```

This script:
- Adds the official Falco repository
- Installs Falco
- Starts the daemon service

### 2. Trigger Events (e.g., run `bash`, edit `/etc/`, spawn shells)

```bash
bash
echo "test" > /etc/falco_test
```

Falco will log alerts for suspicious behavior.

### 3. Parse Falco Alerts

```bash
python3 src/falco_alert_parser.py -l /var/log/falco.log
```

This displays a filtered summary of high-severity alerts and key actions.

## Notes

- Run this on a VM or test machine.
- Falco must run as root to hook into system calls.
- This project helps build detection and response instincts for real environments.
