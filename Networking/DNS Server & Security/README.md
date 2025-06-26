# DNS Server & Security

A lightweight authoritative DNS server built in Python. It serves DNS responses for a predefined list of domains and includes basic security measures such as query logging, denial of unknown requests, and filtering out recursive queries. This simulates core concepts in DNS infrastructure and helps understand potential attack surfaces and mitigations.

## Features

- Minimal authoritative DNS server on UDP port 53
- Serves A records for whitelisted domains only
- Rejects recursive or malformed DNS requests
- Logs all incoming DNS queries with timestamp
- Easily extendable for additional record types

## Usage

```bash
sudo python3 src/dns_server.py
```

## Configuration

Modify the `RECORDS` dictionary in `src/dns_server.py` to add or change which domains are served.

```python
RECORDS = {
    "test.local.": "192.168.1.10",
    "example.local.": "192.168.1.11"
}
```

## Security Features

- Only responds to whitelisted domains
- Ignores recursive DNS queries
- Logs query details for audit and detection
- No recursion, zone transfer, or wildcard handling to minimize attack surface

## Notes

- Requires `sudo` to bind to port 53 (privileged)
- For educational/homelab use — not intended for production deployment
