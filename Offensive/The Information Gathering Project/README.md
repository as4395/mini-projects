# The Information Gathering Project

## Overview
This project automates the collection of publicly available information about a target domain or IP address. It performs reconnaissance using techniques such as DNS enumeration, WHOIS lookup, and subdomain discovery to gather useful intelligence for penetration testing or security assessments.

## Objectives
- Perform DNS enumeration and zone transfers
- Gather WHOIS details about domains/IPs
- Discover subdomains via public sources
- Automate and aggregate information retrieval

## Prerequisites
- Python 3.7+
- Basic networking and DNS knowledge

## Usage

**1.** Clone the repository:
```bash
git clone https://github.com/as4395/Mini-Projects/Offensive/information-gathering.git
cd information-gathering
```
**2.** Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
**3.** Install dependencies:
```
pip install -r requirements.txt
```
**4.** Run the main script to gather information on a target domain:
```
python src/info_gather.py --domain example.com
```

## Notes
- Use responsibly and only against authorized targets.
- Data collected can assist penetration testers during the reconnaissance phase.
