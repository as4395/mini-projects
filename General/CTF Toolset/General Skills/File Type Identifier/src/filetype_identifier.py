import argparse
import sys
import magic

# Define a small map of common magic byte signatures
MAGIC_SIGNATURES = {
    b"\x89PNG\r\n\x1a\n": "PNG Image",
    b"\xff\xd8\xff": "JPEG Image",
    b"%PDF-": "PDF Document",
    b"PK\x03\x04": "ZIP Archive",
    b"MZ": "Windows PE Executable",
    b"\x7fELF": "ELF Executable (Linux)",
    b"GIF89a": "GIF Image",
    b"GIF87a": "GIF Image",
    b"Rar!\x1a\x07\x00": "RAR Archive",
    b"\x1f\x8b": "GZIP Compressed",
    b"\x42\x5a\x68": "BZIP2 Compressed",
    b"\x25\x21\x50\x53": "PostScript Document",
}

def identify_magic_bytes(file_path):
    # Check the file's starting bytes against known magic byte signatures.
    try:
        with open(file_path, "rb") as f:
            file_start = f.read(16)  # Read enough for most magic numbers
            for signature, ftype in MAGIC_SIGNATURES.items():
                if file_start.startswith(signature):
                    return ftype
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        sys.exit(1)
    return "Unknown (magic bytes not recognized)"

def identify_mime_type(file_path):
    # Use libmagic to identify the file's MIME type.
    try:
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)
    except Exception as e:
        print(f"[!] Error detecting MIME type: {e}")
        return "Unknown"

def main():
    parser = argparse.ArgumentParser(description="File Type Identifier using magic bytes and MIME")
    parser.add_argument("file", help="Path to file to analyze")
    args = parser.parse_args()

    file_path = args.file

    print(f"\nAnalyzing file: {file_path}\n")

    # First, try to detect based on known magic byte patterns
    magic_type = identify_magic_bytes(file_path)
    print(f"[+] Magic Byte Signature: {magic_type}")

    # Then try MIME-based detection using libmagic
    mime_type = identify_mime_type(file_path)
    print(f"[+] MIME Type (libmagic): {mime_type}")

if __name__ == "__main__":
    main()
