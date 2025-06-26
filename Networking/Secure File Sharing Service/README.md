# Secure File Sharing Service (SFTP Server & Client)

This project implements a secure file sharing service using Python and the Paramiko library. It includes a standalone SFTP server that accepts uploads from authenticated users and a client-side uploader script for securely sending files. It is useful for homelabs and learning secure protocol use.

## Features

- Secure SFTP server with username/password authentication
- Files uploaded to a chrooted `uploads/` folder (sandboxed)
- Server logs all uploads with timestamp, IP, and filename
- Python client script to securely upload files to the server
- Easily customizable and portable

## Usage

### 1. Install dependencies

```bash
pip install -r requirements/requirements.txt
```

### 2. Run the SFTP server (requires Python 3.8+)

```bash
python3 src/secure_sftp_server.py
```

Server listens on `localhost:2222` and only accepts `testuser` with password `password123`.

### 3. Upload a file using the client uploader

```bash
python3 src/sftp_client_uploader.py -f path/to/file.txt
```

You can modify the host, port, username, or password via CLI arguments.

## Notes

- All uploaded files are stored in `uploads/`
- Server and client communicate over SFTP (via SSH)
- Project is intended for education and internal lab use
