# Disk Image Searcher

## Description
Disk Image Searcher is a command-line tool that allows CTF players and forensic analysts to search through extracted or mounted disk image directories for sensitive keywords. It recursively scans files in a given directory (or mounted image) and flags files containing matching strings. This tool is useful in challenges involving forensic disk analysis, data recovery, or hidden file artifacts.

## Features
- Recursively searches all regular files in a target directory
- Detects matches for user-defined keywords (e.g., flags, secrets, credentials)
- Supports filtering by file extensions or skipping known binary types
- Outputs file paths and matching lines with line numbers
- Designed to work on mounted disk images or extracted file systems

## Installation
Install the required dependencies (only standard library used by default):

```bash
pip install -r requirements/requirements.txt
```

## Usage

```bash
cd src/
python disk_searcher.py --path /mnt/disk_image --keywords flag,password,secret
```

### Optional Arguments:
- `--ext`: Filter by file extensions (e.g., `.txt,.log`)
- `--ignore-binaries`: Skip files likely to be binary

## Notes
- Works best on pre-mounted disk images (e.g., `.img` mounted using loopback).
- This tool does not parse raw partitions or filesystem structures directly.
- For full disk forensic workflows, combine with tools like `binwalk`, `sleuthkit`, or `mount`.
