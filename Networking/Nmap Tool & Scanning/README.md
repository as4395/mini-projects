# Nmap Scanner Wrapper

This tool wraps the functionality of Nmap using Python, allowing automated network scanning with clean, parseable output. It scans a given host or IP range for open ports, identifies running services, and returns the results in a structured format.

## Features

- Wrapper around the `nmap` CLI tool
- Scans for open ports, protocols, and services
- Supports single IPs or CIDR ranges
- Extracts structured data for automation (JSON-style output)
- Clean, easily-readable terminal output

## Usage

```bash
sudo python3 src/nmap_wrapper.py -t <target>
```

Example:
```bash
sudo python3 src/nmap_wrapper.py -t 192.168.1.0/24
```

## Arguments

| Argument | Description |
|----------|-------------|
| `-t`, `--target` | Target IP or subnet (e.g., `192.168.1.1` or `192.168.1.0/24`) |

## Notes

- Requires `nmap` to be installed on your system.
- Must be run with root/sudo to scan all ports and services.
- Output can be extended to write JSON or CSV for post-processing.
