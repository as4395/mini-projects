# OpenVPN Server Automation & Client Management

This project automates the installation and basic configuration of an OpenVPN server on Ubuntu/Debian-based Linux systems. It also provides tools to manage client keys and parse client connection status.

## Features

- Automates OpenVPN server installation and initial configuration
- Generates server and client keys using easy-rsa
- Creates `.ovpn` client configuration files for distribution
- Parses OpenVPN status logs to list connected clients and their IPs

## Usage

### 1. Setup OpenVPN Server

Run the setup script with root privileges:

```bash
sudo python3 src/setup_openvpn.py
```
This script will:

- Install OpenVPN and easy-rsa
- Initialize the Public Key Infrastructure (PKI)
- Generate server and client certificates
- Configure the OpenVPN server with a basic config file
- Start the OpenVPN server service
### 2. Generate Additional Clients
To generate a new client certificate and `.ovpn` config:
```bash
sudo python3 src/setup_openvpn.py --add-client client_name
```
Replace `client_name` with your desired client identifier.

### 3. View Connected Clients
To view currently connected VPN clients, run:
```bash
python3 src/client_status_parser.py -s /etc/openvpn/server/status.log
```
Adjust the status log path if it is different on your system.

## Requirements

- Ubuntu/Debian-based Linux server
- Python 3.7+
- OpenVPN

## Notes

- This is a basic automation for educational and homelab use.
- Proper firewall and network forwarding rules need to be configured separately.
- Running as root or with sudo is necessary for installation and configuration.
