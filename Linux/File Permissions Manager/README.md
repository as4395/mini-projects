# File Permissions Manager

This tool automates the inspection and correction of file permissions on a Linux system. It helps you identify insecure settings like world-writable files and optionally fix them.

## Features

- Recursively scans directories
- Identifies insecure file and directory permissions
- Supports dry-run mode to preview changes
- Interactive fix mode to apply corrections

## Clone the Repository

```bash
git clone https://github.com/as4395/Mini-Projects.git
cd Mini-Projects/Linux/file-permissions-manager
```

## Usage

```bash
python3 src/permissions_manager.py --path /target/dir --fix
```

## Options

| Flag       | Description                            |
|------------|----------------------------------------|
| `--path`   | Target directory to scan               |
| `--fix`    | Automatically fix insecure permissions |
| `--dry`    | Only print results (no changes made)   |

## Example

```bash
python3 src/permissions_manager.py --path /var/www --dry
```

## Requirements

- Python 3.6+
- Root/sudo access (required for applying permission fixes)
