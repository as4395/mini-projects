# Raspberry Pi NAS Server (Linux Project)

This project configures a simple NAS (Network Attached Storage) system using a Raspberry Pi or Linux machine with Samba to securely share folders over the network.

## Features

- Automatically installs and configures Samba
- Creates a shared folder with read/write access
- Automatically starts Samba services
- Adds a user to access the NAS folder

## Requirements

- Linux or Raspberry Pi with `sudo` access
- Python 3.6+
- External or internal storage mounted (optional)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/as4395/Mini-Projects/Linux/nas-server.git
   cd nas-server
   ```

2. Run the setup script:
   ```bash
   sudo python3 src/setup_nas.py
   ```

3. Access the NAS:
   - From Windows: `\\<your-ip>\Share`
   - From Linux: `smb://<your-ip>/Share`

## Security

- For production environments, ensure proper firewall rules and authentication.
- Limit access to specific IP ranges.
