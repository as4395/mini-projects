# Basic Network Scanner

A simple ARP-based network scanner that discovers live hosts on the local network by sending ARP requests to each IP in the target subnet. It is useful for identifying devices on the same LAN for reconnaissance and asset enumeration.
## Features

- Scans local subnet using ARP requests
- Identifies live hosts by IP and MAC address
- Fast and accurate on switched networks
- Built with Scapy for low-level packet manipulation

## Usage

```bash
sudo python3 src/network_scanner.py -t <target-subnet>
```

Example:
```bash
sudo python3 src/network_scanner.py -t 192.168.1.0/24
```

## Arguments

| Argument | Description |
|----------|-------------|
| `-t`, `--target` | Target subnet or IP range in CIDR format (e.g., `192.168.1.0/24`) |

## Notes

- Must be run with root privileges (due to raw socket usage).
- Works on local LAN segments.
- Scapy handles ARP requests efficiently; no ICMP or TCP-based scanning.
