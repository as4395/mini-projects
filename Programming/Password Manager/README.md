# Password Manager

A secure password manager implemented in Python. It allows for creating, storing, retrieving, updating, and deleting passwords encrypted with a master password.

## Features

- Master password authentication to access stored passwords
- Password storage encrypted using AES-256-GCM
- Add, view, update, delete password entries
- CLI interface for easy interaction
- Password entries stored locally in an encrypted JSON file

## Requirements

- Python 3.7+
- `cryptography` package

Install dependencies:

```bash
pip install -r requirements/requirements.txt
```
## Usage

**1:** Run the program:
```bash
python3 src/password_manager.py
```

**2:** Enter your master password. On first run, it will create a new storage file.

**3:** Use the menu to add, view, update, or delete password entries.

## Security Notes

- The master password is never stored. Remember it to access your passwords.
- Data is encrypted locally; do not share the storage file.
- Suitable for personal, offline use and learning purposes.
