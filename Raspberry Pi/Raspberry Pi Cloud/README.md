# Raspberry Pi Cloud

## Overview

This project transforms your Raspberry Pi into a lightweight, self-hosted cloud file storage service using `Flask` and `Paramiko`. It allows uploading, downloading, and managing files from the local network or the internet (when port-forwarded). It simulates a mini Dropbox-style server for home or small office usage.

## Features

- Web-based upload/download interface
- Optional SFTP access via Paramiko
- AES-256 encryption for secure storage
- User authentication with password protection
- Configurable upload/download directory

## Setup Instructions

### 1. Prerequisites

- A Raspberry Pi running Raspberry Pi OS (or any Linux distro)
- Python 3.8+
- `pip` installed
- Basic networking knowledge (for port forwarding if external access is required)

### 2. Installation

```bash
git clone https://github.com/as4395/Mini-Projects/RaspberryPi/RaspberryPi-Cloud.git
cd RaspberryPi-Cloud
pip install -r requirements.txt
```
### 3. Running the App
```bash
python3 src/server.py
```
Then visit `http://<raspberrypi-ip>:5000` in your browser.

### 4. Credentials
Default credentials:

  Username: `admin`

  Password: `raspberry`

Change them in the `config.json file` after first run.

## Security Notes

- AES-256-CBC is used for file encryption with a derived key from the user's password.
- HTTPS is recommended when exposing the server externally.
- Default credentials must be changed in production.

## Optional: SFTP Access

The script can optionally run an SFTP server on port 2222 using Paramiko. Enable it by editing `config.json`:
```json
"sftp_enabled": true
```
