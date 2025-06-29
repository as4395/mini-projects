# Linux Router Configuration

## Overview
This project converts a Linux machine into a basic router by configuring network interfaces, enabling IP forwarding, and setting up NAT using iptables. It demonstrates script-based network routing setup.

## Features
- Enables IP forwarding
- Configures NAT (masquerading)
- Adds or removes network forwarding rules
- CLI interface for interactive setup

## Requirements
- Linux system with at least two network interfaces (e.g., eth0 and eth1)
- Python 3.7+

## Setup & Usage
```bash
git clone https://github.com/as4395/Mini-Projects/Linux/router-setup.git
cd router-setup
sudo python3 src/router_setup.py --lan eth0 --wan eth1 --action enable
```

## Examples
```bash
sudo python3 src/router_setup.py --lan eth0 --wan eth1 --action enable
sudo python3 src/router_setup.py --lan eth0 --wan eth1 --action disable
```

## Warning
Running these commands will alter your system's network settings. Use in test environments only.
