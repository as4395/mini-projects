# Honeypot Testing

This project automates the setup and configuration of the Cowrie SSH honeypot in a local environment and provides a Python log parser to analyze attacker activity.

## Features

- Automated Cowrie installation and configuration script
- Runs Cowrie honeypot (SSH emulation) locally
- Parses Cowrie JSON log files to extract login attempts, commands, and credentials
- Logs saved in `cowrie/var/log/cowrie/`
- Useful for capturing attacker behavior and credential harvesting

## Prerequisites

- Linux environment (Ubuntu recommended)
- Python 3.8+
- Git, virtualenv, build tools installed

## Usage

1. **Install & configure Cowrie** (run once):

```bash
python3 src/setup_cowrie.py
```

2. **Run the Cowrie honeypot** (from `cowrie` directory):

```bash
cd cowrie
bin/cowrie start
```

3. **Parse Cowrie logs** (run anytime to analyze attacker activity):

```bash
python3 src/cowrie_log_parser.py -l cowrie/var/log/cowrie/combined.log
```

## Notes

- Cowrie runs as a daemon simulating SSH and capturing attacker commands
- This setup does not require root but does require installing dependencies
- Logs are in JSON format; parser extracts useful info for quick review
