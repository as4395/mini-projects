# Packet Sniffer

A basic but powerful packet sniffer built using Scapy. It captures live network traffic from a specified interface and displays key details such as source/destination IP, protocol, and port information. This tool is useful for learning how network traffic flows and in threat hunting scenarios.

## Features

- Real-time packet capture
- Protocol identification (TCP, UDP, ICMP, etc.)
- Extracts key packet metadata: source/destination IPs, ports, protocols
- Filters out irrelevant packets for clean output
- Optional interface selection

## Usage

```bash
sudo python3 src/packet_sniffer.py -i <interface>
```

Example:
```bash
sudo python3 src/packet_sniffer.py -i eth0
```

## Arguments

| Argument | Description |
|----------|-------------|
| `-i`, `--interface` | Network interface to sniff on (required) |

## Notes

- Requires root privileges to access raw sockets.
- Only captures IPv4 packets.
- Designed to be readable, extendable, and usable for forensic analysis.
