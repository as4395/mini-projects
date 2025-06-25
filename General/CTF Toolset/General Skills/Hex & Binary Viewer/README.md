# Hex & Binary Viewer

## Description
This tool is a minimalist hex and binary viewer designed for CTF participants and forensic analysts who need to inspect the raw contents of files. It displays file data in both hexadecimal and ASCII formats, allowing for easy identification of patterns, offsets, and printable data. It is ueful for identifying embedded metadata, obfuscated flags, and magic headers.

## Features
- Reads and displays raw bytes from a file
- Shows both hex representation and ASCII side-by-side
- Displays byte offsets in a structured format
- Allows selection of offset and length for targeted inspection
- CLI-based and Python 3.7+ compatible

## Installation

Install the required packages (only standard library used, but `argparse` is required):

```bash
pip install -r requirements/requirements.txt
```

## Usage

```bash
python hex_binary_viewer.py --file target.bin --offset 0 --length 512
```
-`--file`: Path to the binary file you want to inspect.
-`-offset`: Byte offset to start viewing from (default: 0).
-`-length`: Number of bytes to view (default: 256).

## Notes

- Tool does not modify any file — it is strictly for viewing.
- ASCII output will show dots (`.`) for non-printable characters.
- Intended for use in CTFs and binary analysis environments.
