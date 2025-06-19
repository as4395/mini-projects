# Safe Folder App with Password

## Description
This application allows you to securely manage access to a protected folder using a password. It supports viewing, adding, and deleting files inside the safe folder, and encrypts file contents to prevent unauthorized access. All sensitive operations are protected by a master password which is hashed and stored locally. Files are encrypted on disk using symmetric encryption (AES-256), and only decrypted when accessed through the application.

## Features
- Secure master password authentication
- Add files to a protected folder with encryption
- View a list of encrypted files
- Decrypt and view file contents securely
- Delete files from the safe folder
- Uses symmetric encryption (AES-256)
- Stores passwords using salted hashing (PBKDF2-HMAC)

## Installation
Install the required Python packages using the command below:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Run the application from the ```src``` directory:

```bash
cd src/
python safe_folder.py
```
On first run, you will be prompted to set a master password. This password will be securely hashed and stored locally. All future access requires this password.

## Notes

- Encrypted files are stored in the ```safe_data/``` directory.
- File names remain unchanged but file contents are encrypted.
- Encryption keys are derived from the master password with PBKDF2 and a random salt.
- Intended for educational and personal use; not suitable for high-security needs without further enhancements.
