# Deep Packet Inspection (DPI) Tool

This project is a Deep Packet Inspection (DPI) tool designed to analyze live network traffic in detail. It captures and decodes packets, inspects payloads, and detects application-layer protocols (e.g., HTTP, DNS, FTP). It is useful for traffic analysis, malware detection, and educational insight into how DPI systems work.

## Features

- Captures live packets on a specified interface
- Analyzes each packet up to the application layer
- Detects and logs common protocols (HTTP, DNS, FTP, etc.)
- Displays payload content where applicable
- Filters out irrelevant packet types for clarity

## Usage

**1.** Run the tool with administrative/root privileges:

```bash
sudo python3 src/dpi_inspector.py -i <interface>
```
**2.** Example:
```bash
sudo python3 src/dpi_inspector.py -i eth0
```
**3.** Press `Ctrl+C` to stop the packet capture at any time.

## Requirements
- Python 3.7+
- Scapy

## Security Note

This tool is for educational and ethical testing purposes only. Do not run on networks without authorization.
