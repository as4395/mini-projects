import os
import sys
import argparse
import imghdr
from pathlib import Path
from typing import List

from PIL import Image
from stegano import lsb
import binascii

COMMON_SIGNATURES = [
    b"\x89PNG",       # PNG signature
    b"\xFF\xD8\xFF",  # JPEG signature
    b"GIF89a",        # GIF signature
    b"BM",            # BMP signature
]

def is_image(file_path: Path) -> bool:
    # Check if the file is a valid image using imghdr.
    return imghdr.what(file_path) is not None

def check_for_lsb(path: Path) -> bool:
    # Attempt to reveal hidden LSB data in the image.
    try:
        message = lsb.reveal(str(path))
        return message is not None
    except Exception:
        return False

def check_for_extra_data(path: Path) -> bool:
    # Check for appended data after image file end markers.
    try:
        with open(path, "rb") as f:
            data = f.read()
        # JPEG and PNG end markers
        eof_markers = [b'\xFF\xD9', b'IEND\xAE\x42\x60\x82']
        for marker in eof_markers:
            if marker in data:
                end = data.find(marker) + len(marker)
                trailing = data[end:]
                if trailing.strip():
                    return True
        return False
    except Exception:
        return False

def scan_file(path: Path):
    print(f"\n[+] Scanning: {path.name}")

    if not is_image(path):
        print("  [-] Not a valid image format. Skipping.")
        return

    if check_for_lsb(path):
        print("  [*] LSB data detected.")

    if check_for_extra_data(path):
        print("  [*] File contains extra appended data (possible steg).")

def find_images(folder: Path) -> List[Path]:
    # Recursively find all image files in a given folder.
    return [f for f in folder.rglob("*") if f.is_file() and is_image(f)]

def main():
    parser = argparse.ArgumentParser(description="StegoScan - Basic Image Steganography Scanner")
    parser.add_argument("path", help="Path to image file or directory")
    args = parser.parse_args()

    input_path = Path(args.path)

    if not input_path.exists():
        print("[-] Path does not exist.")
        sys.exit(1)

    targets = [input_path] if input_path.is_file() else find_images(input_path)

    if not targets:
        print("[-] No valid image files found.")
        sys.exit(1)

    for img in targets:
        scan_file(img)

if __name__ == "__main__":
    main()
