# File Type Identifier

## Description
This tool identifies the true type of a file based on its magic bytes and MIME type. It is useful for analyzing files in CTFs where extensions may be intentionally misleading. It uses both a local signature check and the `python-magic` library for MIME inspection.

## Features
- Detects file type using known magic byte signatures
- Uses libmagic to fetch MIME type
- Supports various common formats: PNG, JPEG, PDF, ZIP, ELF, PE, etc.
- Helpful in forensics and stego-based challenges

## Installation
Install the required Python packages:

```bash
pip install -r requirements/requirements.txt
```
**Note:** On Linux/macOS, you may need to install libmagic via your package manager:

### Ubuntu/Debian
```bash
sudo apt install libmagic1
```

### macOS (Homebrew)
```bash
brew install libmagic
```

## Usage
```bash
python filetype_identifier.py /path/to/suspicious/file
```

## Notes

- Some formats may not be detected by magic bytes alone.
- Works best when combined with other tools (e.g., hex viewer or binwalk).
