# Centralized Syslog Server

This project sets up a basic centralized Syslog server on a Linux machine. It captures, stores, and organizes log messages from other devices and services using the Syslog protocol (UDP 514). This is useful for centralized logging in homelab or production environments.

## Features

- Receives Syslog messages over UDP
- Stores logs into organized files based on date and hostname
- Includes a simple CLI viewer for recent logs
- Runs as a background listener using Python's `socketserver`

## Requirements

- Python 3.7+
- Root or elevated privileges (to bind port 514)
- Linux with rsyslog or compatible devices that support remote logging

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/as4395/Mini-Projects/Linux/centralized-syslog-server.git
   cd centralized-syslog-server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Syslog server (requires root for port 514):
   ```bash
   sudo python3 src/syslog_server.py
   ```

4. (Optional) View recent logs:
   ```bash
   python3 src/view_logs.py
   ```

## Example Syslog Message (UDP 514)
To test locally:
```bash
logger -n 127.0.0.1 -P 514 "This is a test message"
```

## Security Note
For production, consider using TCP + TLS with rsyslog or syslog-ng for encrypted and reliable log forwarding.
