# Static String Extractor

## Description
This tool extracts printable ASCII and Unicode strings from executable files such as ELF, PE, or Mach-O binaries. It's useful for reverse engineering, CTF analysis, and static inspection of unknown binaries. You can optionally filter extracted strings using regular expressions or keyword patterns to focus on useful indicators like hardcoded credentials, URLs, file paths, or flags.

## Features
- Extracts both ASCII and UTF-16LE strings from binary files
- Allows filtering output with keywords or regex
- Supports minimum string length filtering
- Designed to work on Linux, macOS, and Windows binaries

## Installation
Install required dependencies (only for regex filtering):

```bash
pip install -r requirements/requirements.txt
```

## Usage

```bash
python3 string_extractor.py <path_to_binary> [--min-length N] [--filter "regex|keyword"]
```
Examples
Extract default strings:
```bash
python3 string_extractor.py suspicious_binary
```
Extract strings with minimum length 6:
```bash
python3 string_extractor.py malware_sample --min-length 6
```
Filter strings containing 'password':
```bash
python3 string_extractor.py dump.bin --filter password
```
Use regex to find flags:
```bash
python3 string_extractor.py dump.bin --filter "CTF{.*?}"
```

## Notes

- Strings are extracted statically and no execution or sandboxing is involved.
- Regex is optional but useful to hone in on meaningful content.
- UTF-16LE decoding helps with Windows-targeted binaries.
