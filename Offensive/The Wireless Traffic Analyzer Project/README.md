# Wireless Traffic Analyzer

## Overview

This tool captures and analyzes nearby wireless traffic using monitor mode on a wireless interface. It passively detects Access Points (SSIDs), associated clients, MAC addresses, and signal strength.

## Features

- Detects wireless Access Points (SSID, MAC, Channel, Signal)
- Detects client devices and their associated APs
- Logs discovered devices to terminal or file
- Works in monitor mode (requires compatible Wi-Fi adapter)

## Usage

> Ensure your wireless adapter is set to monitor mode using `airmon-ng` or similar tools before running this script.

### Example (after setting `wlan0` to monitor mode):

```bash
sudo python3 src/wifi_sniffer.py --interface wlan0mon --output scan_results.txt
```
# Requirements

- Python 3+
- Scapy
- Root privileges
- Wireless adapter supporting monitor mode

## Setup
```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```
## Enabling Monitor Mode (manually):
```bash
sudo apt install aircrack-ng
sudo airmon-ng start wlan0
```

## Disclaimer

Use this tool only in environments where you have permission to monitor wireless traffic.
