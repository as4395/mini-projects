# Configure a Firewall in Linux

## Overview
This project demonstrates how to configure a Linux-based firewall using both `iptables` and `ufw`. You can define rules to allow or block incoming/outgoing traffic based on IP addresses, protocols, or port numbers. This provides the foundational layer of host-based network security.

## Features
- Basic and advanced `iptables` rules
- Simple `ufw` wrapper for quick setup
- Logging support
- Interactive CLI for firewall configuration

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/as4395/Mini-Projects/Linux/firewall-setup.git
cd firewall-setup
```

### 2. Run the setup tool
```bash
sudo python3 src/firewall_configurator.py
```

## Supported Commands
- Allow/Deny specific ports
- Block IP addresses
- Enable logging
- Flush all rules
- List current rules

## Example Usage
```bash
sudo python3 src/firewall_configurator.py --mode iptables --block-port 23
sudo python3 src/firewall_configurator.py --mode ufw --allow-port 22
```

## Requirements
- Python 3.7+
- Linux system with `iptables` or `ufw` installed

## Disclaimer
This tool modifies live firewall settings. Use with caution and test in a virtual machine before applying to production systems.
