# Linux Backup Server Setup

## Overview
This project builds a simple backup server using Python. It watches a source directory and backs up changed files to a remote destination (local or over SSH) with versioned backups.

## Features
- Incremental backups with timestamped folders
- Optional remote backup via SCP
- CLI tool for managing backups
- Logging of backup operations

## Requirements
- Python 3.7+
- `watchdog` and `paramiko` packages
- SSH access if remote backup is enabled

## Setup & Usage
```bash
git clone https://github.com/as4395/Mini-Projects/Linux/backup-server.git
cd backup-server
pip install -r requirements.txt
```

# Run local backup:
```bash
python3 src/backup_server.py --source /home/pi/documents --dest /mnt/backup
```

# Run remote backup:
```bash
python3 src/backup_server.py --source ~/docs --dest-server user@backup:/backups
```

## Notes
- Dest path is created if it doesn't exist.
- Remote backups are conducted via SCP over SSH.
