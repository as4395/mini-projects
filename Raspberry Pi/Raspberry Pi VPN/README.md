# Raspberry Pi VPN Setup with PiVPN (WireGuard)

This project automates the installation and configuration of a secure VPN server using PiVPN (WireGuard) on a Raspberry Pi. The script uses system commands to install the VPN, configure users, and export client `.conf` files.

## Overview

Use PiVPN to create a VPN server on a Raspberry Pi. 


Connect to the Pi server over a public network to secure a connection. 

This automation script handles the setup process and generates configuration files for VPN clients.

## Features

- Installs PiVPN (WireGuard) using official installer
- Adds VPN client users via interactive prompt
- Exports client configuration files to a local directory
- Lightweight and production-quality Python automation

## Requirements

- Raspberry Pi with Raspberry Pi OS
- sudo/root access
- Static IP or Dynamic DNS configured
- Internet connection

## Python Dependencies

Install using:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:

```bash
https://github.com/as4395/Mini-Projects.git
cd raspberry-pi-vpn
```

2. Run the setup script:

```bash
sudo python3 src/setup_vpn.py
```

3. Follow the prompts:
   - Installs PiVPN
   - Adds VPN user
   - Saves client `.conf` to `client_configs/`

4. Transfer the client `.conf` file securely to the device that will connect to the VPN.

## Generated Files

- `client_configs/<username>.conf` - WireGuard client configuration file

## Security Notes

- Use strong passwords when prompted
- Restrict SSH access (change port, use key-based authentication)
- Open only required ports (e.g., 51820/UDP for WireGuard)
- Consider setting up a firewall (e.g., UFW)

## References

- https://pivpn.io
- https://github.com/pivpn/pivpn
- https://www.wireguard.com
