# DNS Recon Tool

## Description
The DNS Recon Tool performs automated DNS enumeration to discover subdomains and gather DNS records for a target domain. It supports common record types like A, AAAA, MX, NS, TXT, and CNAME. This tool helps during penetration testing and CTF challenges to identify attack surfaces and network infrastructure.

## Features
- Enumerates subdomains from a wordlist or user input
- Retrieves DNS record types: A, AAAA, MX, NS, TXT, CNAME
- Handles DNS query timeouts and errors gracefully
- Outputs discovered records in a readable format
- Supports command line arguments for domain and wordlist input

## Installation
Install the required Python packages:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Run the tool specifying the target domain and optional subdomain wordlist:
```bash
python dns_recon.py --domain example.com --wordlist wordlist.txt
```
- `--domain` (required): Target domain for DNS enumeration.
- `--wordlist` (optional): Path to a file containing subdomains to test.


## Notes

- Requires internet access to perform DNS queries.
- Uses `dnspython` for DNS operations.
- Designed for ethical use on authorized targets only.
