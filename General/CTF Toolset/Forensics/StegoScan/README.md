# StegoScan – Image Steganography Detector

## Description
StegoScan is a forensic analysis tool for detecting hidden data in image files using common steganographic techniques. It scans JPEG and PNG files for signatures of tools like `steghide`, `zsteg`, `exiftool`, and more. The goal is to automate the early stage of CTF image forensics by rapidly identifying possible data-hiding anomalies.

## Features
- Detects embedded files using `binwalk`
- Extracts and analyzes metadata using `exiftool`
- Detects LSB and other patterns using `zsteg` (if available)
- CLI tool for scanning single images or folders of images
- Auto-recognition of common stego tools and formats

## Installation
Install the required Python packages:

```bash
pip install -r requirements/requirements.txt
```
Install required tools:
```bash
# exiftool must be installed
sudo apt install libimage-exiftool-perl

# binwalk must be installed
sudo apt install binwalk

# Optional but recommended for PNGs
gem install zsteg
```

## Usage

```bash
cd src/
python stegoscan.py --file ../samples/image1.jpg
python stegoscan.py --dir ../samples/
```

## Notes

- Works on `.jpg`, `.jpeg`, and `.png` files.
- Some detections (like zsteg) only work on specific image formats.
Tool is meant for use in CTF challenges and educational contexts.
