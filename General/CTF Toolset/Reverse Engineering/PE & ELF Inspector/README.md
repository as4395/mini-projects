# PE/ELF Inspector

## Description
This tool provides metadata and section-level insights into executable files, including both Windows PE (Portable Executable) and Linux ELF (Executable and Linkable Format) binaries. It helps CTF players and reverse engineers quickly examine key attributes like section headers, imports, architecture, and symbols.
It is useful for identifying packing, architecture mismatches, and hinting at embedded data or obfuscation.

## Features
- Detects and parses both PE and ELF binary formats
- Displays architecture, entry point, sections, symbols, and imports
- Color-coded output for improved readability
- Auto-detects file type based on magic bytes
- Cross-platform (Linux, macOS, Windows)

## Installation

Install required Python dependencies:
```bash
pip install -r requirements/requirements.txt
```

### Usage

From the ```src/``` directory:
```bash
python inspector.py /path/to/binary
```
Example
```bash
python inspector.py samples/test_elf
python inspector.py samples/test_pe.exe
```

## Notes

- Requires Python 3.7+
- Supports static inspection only — does not emulate or run binaries
- For ELF files, symbols and headers depend on debug symbols being present
Built for CTF use; not a full substitute for readelf or objdump
