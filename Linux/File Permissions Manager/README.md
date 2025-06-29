# File Permissions Manager

This tool automates the inspection and modification of file permissions across a Linux system. It allows you to list world-writable files, incorrect permission settings, and fix common misconfigurations interactively.

## Features

- Lists files with insecure permissions
- Fixes common permission issues
- Recursively audits directories
- Supports dry-run mode for review

## Usage

```bash
python3 src/permissions_manager.py --path /target/dir --fix
```

## Options

| Flag       | Description                     |
|------------|---------------------------------|
| `--path`   | Target directory                |
| `--fix`    | Auto-fix insecure permissions   |
| `--dry`    | Only print results (no changes) |

## Example

```bash
python3 src/permissions_manager.py --path /var/www --dry
```

## Requirements

- Python 3
- sudo/root access (for changes)
