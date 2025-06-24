# Packet Sniffer CLI

## Description

A lightweight command-line tool that captures and displays live network packets using raw sockets. It is designed for CTFs and traffic analysis during network-based challenges.

## Features

- Captures and parses packets in real time
- Supports TCP, UDP, and ICMP filtering
- Displays key packet details: IPs, ports, flags, and lengths
- Optional hex + ASCII dump of packet payloads
- Interface selection (Linux/macOS only)

## Usage

```bash
sudo python packet_sniffer.py [--iface eth0] [--proto tcp] [--hexdump]
```

## Arguments

| Argument     | Description                                  | Required | Default |
|--------------|----------------------------------------------|----------|---------|
| `--iface`    | Interface to sniff on (e.g., eth0)           | No       | First found |
| `--proto`    | Protocol filter: `tcp`, `udp`, `icmp`, `all` | No       | `all`    |
| `--hexdump`  | Include hex+ASCII dump of payload            | No       | False    |

## Example

```bash
sudo python packet_sniffer.py --iface eth0 --proto tcp --hexdump
```

## Output

```
[10.0.0.5:443] → [10.0.0.2:52014] | TCP | Flags: PA | Len: 98
[10.0.0.2] → [10.0.0.5] | ICMP | Echo request | Len: 64
...
```

## Notes

- Requires root privileges to create raw sockets.
- Tested on Linux and macOS. Not supported on Windows.
