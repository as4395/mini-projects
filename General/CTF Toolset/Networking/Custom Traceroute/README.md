# Custom Traceroute

## Description
This tool implements a custom traceroute utility using ICMP echo requests and Time-To-Live (TTL) manipulation. It helps visualize the path packets take to reach a remote host, resolve intermediate hops via reverse DNS, and measure response latency per hop.

## Features
- Sends ICMP Echo Requests with increasing TTL values
- Captures responses to identify each hop along the route
- Reports IP addresses, hostnames (if resolvable), and round-trip times
- Gracefully handles timeouts and unreachable hops
- Works on Linux/macOS (requires root privileges)

## Installation
Install the required packages with:

```bash
pip install -r requirements/requirements.txt
```
**Note:** You must run the script with elevated privileges (e.g., `sudo`) to send raw ICMP packets.

## Usage
```bash
sudo python traceroute.py <target_host>
```
Example:
```bash
sudo python traceroute.py google.com
```
- Supports IPv4 addresses or domain names
- Defaults to 30 hops with 2-second timeout per hop

## Notes
- Uses raw sockets to send and receive ICMP packets
- Reverse DNS lookup is optional and falls back to IP if hostname resolution fails
- Developed for CTF diagnostics and educational use
