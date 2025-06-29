# Linux Router Setup

This project sets up a basic router using a Linux machine to enable IP forwarding, NAT (using iptables), DHCP, and DNS resolution between two interfaces (LAN and WAN). It simulates a router within a virtual lab.

## Features

- Enables packet forwarding
- Uses `iptables` for NAT (Masquerading)
- Assigns IPs on internal network via DHCP
- Configures `dnsmasq` for DNS and DHCP
- Simple interface management

## Requirements

- Linux machine with 2 network interfaces (e.g., `eth0` for WAN, `eth1` for LAN)
- Root privileges

## Installation

```bash
sudo apt update && sudo apt install -y iptables dnsmasq net-tools
```

## Usage

```bash
sudo python3 src/setup_router.py
```

## Example

- WAN: `eth0` connected to external network
- LAN: `eth1` serves internal clients

## Security Tip

Don't expose unnecessary services on the WAN side. Add `iptables` rules as needed to filter incoming traffic.

