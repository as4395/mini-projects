# Hash Identifier & Cracker

## Description
This tool helps identify common hash formats (e.g., MD5, SHA1, SHA256) and attempts to crack hashes using a user-supplied wordlist. It's designed for quick use during CTFs when faced with unknown or weakly hashed passwords.

## Features
- Identifies hash type based on length and known patterns
- Supports MD5, SHA1, SHA256, SHA384, SHA512, NTLM
- Brute-force cracking against a wordlist
- Clean command-line interface

## Installation

Install required packages with:

```bash
pip install -r requirements/requirements.txt
````

## Usage

```bash
python hash_cracker.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist rockyou.txt
```
You can also supply a known hash type:
```bash
python hash_cracker.py --hash e99a18c428cb38d5f260853678922e03 --wordlist wordlist.txt --type md5
```

## Notes

- Use a strong and relevant wordlist for better results.
- For NTLM hashes, ensure your wordlist uses correct case (it's case-sensitive).
- This tool does not perform rainbow table lookups or GPU-based cracking.
