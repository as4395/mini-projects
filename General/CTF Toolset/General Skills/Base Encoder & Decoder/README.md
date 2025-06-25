# Base Encoder/Decoder

## Description
A simple CLI tool to encode or decode strings using various base encodings commonly encountered in CTFs. It supports base16, base32, base64, and base85. Automatically detects base when decoding, if possible.

## Features
- Encode a string in multiple base formats
- Decode a given base-encoded string
- Auto-detection of base encoding (for known formats)
- Supports base16, base32, base64, and base85

## Installation
Install the required dependencies (Python 3.7+ is required):

```bash
pip install -r requirements/requirements.txt
```

## Usage

### Encode a String
```bash
python basecoder.py --encode "ctf{example}"
```
### Decode a String
```bash
python basecoder.py --decode "Y3RmZXhhbXBsZQ=="
```

## Notes

- If decoding fails, try manually specifying or testing another base format.
- Handles padding and normalization automatically.
