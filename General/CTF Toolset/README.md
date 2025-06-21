# 🛠️ Capture The Flag (CTF) Tool Set – Custom Built

## 📋 Description
This repository is a curated set of offensive and investigative tools developed specifically for use in Capture The Flag (CTF) competitions. Each tool is organized by CTF category and focuses on solving a recurring type of challenge seen in beginner to intermediate competitions. These tools are designed to save time during contests, provide hands-on understanding of core techniques, and can be extended for personal use.

---

## 🧩 Categories Covered

- Web Exploitation
- Cryptography
- Reverse Engineering
- Forensics
- OSINT (Open-Source Intelligence)
- Networking
- Binary Exploitation
- General Skills

---

## 🧰 Tools Included

### Web Exploitation
- **AutoSQLi Scanner**: Automated SQL Injection testing and exploitation tool.
- **Header Analyzer**: Extracts and interprets suspicious HTTP headers.
- **Session Cookie Decoder**: Decodes and analyzes web session cookies.

### Cryptography
- **Cipher AutoSolver**: Detects and solves Caesar, Vigenère, and substitution ciphers.
- **Hash Identifier & Cracker**: Identifies hash algorithms and brute-forces known hashes.
- **AES Encryptor/Decryptor**: CLI utility for AES-256-CBC file and string encryption/decryption.

### Reverse Engineering
- **Static String Extractor**: Pulls readable strings from binaries and flags suspicious content.
- **Custom Disassembler Wrapper**: Wraps ```capstone``` disassembly with simplified CLI interface.
- **PE/ELF Inspector**: Scans metadata and sections for clues in executables.

### Forensics
- **StegoScan**: Automatically checks images for common steganographic signatures.
- **PCAP Feature Extractor**: Filters and summarizes PCAP files for protocols, passwords, and anomalies.
- **Disk Image Searcher**: Keyword searches across mounted or extracted disk images.

### OSINT
- **Username Profiler**: Queries multiple sites for a username's presence.
- **Metadata Extractor**: Extracts GPS and author data from images and documents.
- **Email Verifier**: Lightweight verifier of email domain, DNS, and MX records.

### Networking
- **Port Sweep CLI**: Fast TCP/UDP scanner using ```asyncio```.
- **DNS Recon Tool**: Enumerates subdomains and records using DNS queries.
- **Custom Traceroute**: ICMP-based traceroute with TTL timing and reverse DNS lookup.

### Binary Exploitation
- **ROP Gadget Finder**: Scans binaries for Return-Oriented Programming gadgets.
- **Buffer Overflow Auto-Payload Generator**: Generates pattern strings and offsets for overflow testing.
- **Format String Exploiter**: Assists in payload crafting for format string attacks.

### General
- **Base Encoder/Decoder**: Converts between base16/base32/base64/base85.
- **File Type Identifier**: Uses magic bytes and MIME type to verify actual file types.
- **Hex & Binary Viewer**: Minimalist CLI viewer with offset navigation and ASCII rendering.

---

## 🛠️ How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/as4395/CTF_Toolset.git
   cd CTF_Toolset
   ```

2. Navigate to any category folder (e.g., `cryptography/`) to use or modify the tools.

3. Install dependencies (if any) using:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tool as needed:
   ```bash
   python3 toolname.py
   ```

---

## 📝 Notes

- All tools are written in Python for ease of use, and require Python 3.7+.
- Tools are standalone and do not require internet access unless OSINT-based.
- Designed for fast use during timed competitions — speed and reliability prioritized.
- This is not a replacement for understanding — each tool is documented to help you learn.
- All code is for **educational and ethical CTF use only**.
