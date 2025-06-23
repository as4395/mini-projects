# PCAP Feature Extractor

## Description
This tool analyzes `.pcap` (packet capture) files to extract useful features relevant to forensic and CTF analysis. It provides a summarized view of protocols, packet counts, credential leaks, DNS queries, and potential anomalies. The tool is helpful for quickly identifying points of interest in network traffic without manual inspection in Wireshark.

## Features
- Summarizes packet counts by protocol (TCP, UDP, ICMP, etc.)
- Extracts HTTP credentials (Basic Auth)
- Extracts DNS queries and responses
- Identifies unusual or high-frequency IPs
- Displays file transfer attempts (FTP, HTTP downloads)
- Detects potential cleartext password leaks in payloads

## Installation

Install required dependencies:
```bash
pip install -r requirements/requirements.txt
```

## Usage

Run the tool on a `.pcap` file like this:
```bash
python pcap_extract.py path/to/capture.pcap
```
Example:
```bash
python pcap_extract.py network_dump.pcap
```

## Notes

- This tool is built on `scapy`, which requires administrative privileges on some systems.
- It does not reassemble fragmented packets or TCP streams fully; intended for fast reconnaissance.
- Designed for CTFs and learning — not intended as a full PCAP analysis suite.
