# Linux Backup Server

A Python-powered Linux backup server using `rsync` to automate backups of specified directories.
This simulates how a real backup server would function in a home or small-office environment.

## Features

- Schedule local backups of important files/folders.
- Preserve timestamps, permissions, and symbolic links.
- Log backup activities with success/failure status.

## Requirements

- Python 3.7+
- rsync (installed on system)

## Usage

```bash
git clone https://github.com/as4395/Mini-Projects.git
cd Mini-Projects/Linux/backup-server
python3 src/backup_server.py --source /path/to/source --destination /path/to/backup --log backup.log
```

## Example

```bash
python3 src/backup_server.py --source ~/Documents --destination /mnt/backup_drive --log backup.log
```
