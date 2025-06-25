import argparse
import os

def is_printable(byte):
    # Check if a byte corresponds to a printable ASCII character.
    return 32 <= byte <= 126

def read_file_bytes(path, offset, length):
    # Read a chunk of bytes from the file starting at a given offset.
    try:
        with open(path, "rb") as f:
            f.seek(offset)
            return f.read(length)
    except Exception as e:
        print(f"[!] Failed to read file: {e}")
        return None

def display_hex_and_ascii(data, start_offset):
    """Display data in hex + ASCII side-by-side, similar to hexdump."""
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_bytes = ' '.join(f"{b:02x}" for b in chunk)
        ascii_text = ''.join(chr(b) if is_printable(b) else '.' for b in chunk)
        print(f"{start_offset + i:08x}  {hex_bytes:<48}  {ascii_text}")

def main():
    parser = argparse.ArgumentParser(description="Hex & Binary Viewer")
    parser.add_argument("file", help="Path to file")
    parser.add_argument("--offset", type=int, default=0, help="Start offset (default: 0)")
    parser.add_argument("--length", type=int, default=256, help="Number of bytes to display (default: 256)")
    args = parser.parse_args()

    file_path = args.file

    if not os.path.isfile(file_path):
        print("[!] File does not exist.")
        return

    data = read_file_bytes(file_path, args.offset, args.length)
    if data is None:
        return

    display_hex_and_ascii(data, args.offset)

if __name__ == "__main__":
    main()
