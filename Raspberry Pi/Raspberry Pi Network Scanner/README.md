# Raspberry Pi Network Scanner

This project builds a lightweight ARP-based network scanner in Python, designed to run on a Raspberry Pi. It identifies all active devices in a given subnet by sending ARP requests and parsing the responses.

## Features

- Fast ARP-based device discovery
- Displays IP, MAC, and vendor information
- Designed to run on Raspberry Pi with minimal resources
- Clean CLI interface

## Setup Instructions

### 1. Install required dependencies
```bash
sudo apt update
sudo apt install python3-scapy net-tools
```
### 2. Run the script
```bash
sudo python3 src/pi_network_scanner.py
```
### Example Output

```
IP Address       MAC Address          Vendor
192.168.0.1      11:22:33:44:55:66    TP-Link
192.168.0.101    AA:BB:CC:DD:EE:FF    Apple
```
## Notes

- Must be run with `sudo` to access network interface for ARP scanning.
- Works best in local/home networks (LAN) on Raspberry Pi.
