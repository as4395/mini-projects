import argparse
import re
import sys
from pathlib import Path

def extract_ascii(data: bytes, min_length: int):
    result = []
    current = bytearray()
    for byte in data:
        if 32 <= byte <= 126:
            current.append(byte)
        else:
            if len(current) >= min_length:
                result.append(current.decode('ascii'))
            current.clear()
    if len(current) >= min_length:
        result.append(current.decode('ascii'))
    return result

def extract_utf16le(data: bytes, min_length: int):
    result = []
    current = bytearray()
    i = 0
    while i < len(data) - 1:
        if data[i+1] == 0 and 32 <= data[i] <= 126:
            current += data[i:i+2]
            i += 2
        else:
            if len(current) >= min_length * 2:
                try:
                    result.append(current.decode('utf-16le'))
                except UnicodeDecodeError:
                    pass
            current = bytearray()
            i += 1
    if len(current) >= min_length * 2:
        try:
            result.append(current.decode('utf-16le'))
        except UnicodeDecodeError:
            pass
    return result

def filter_strings(strings, pattern):
    try:
        regex = re.compile(pattern)
        return [s for s in strings if regex.search(s)]
    except re.error:
        # Treat as plain keyword if not a valid regex
        return [s for s in strings if pattern in s]

def main():
    parser = argparse.ArgumentParser(description="Extract printable strings from binary files.")
    parser.add_argument("binary", help="Path to binary file")
    parser.add_argument("--min-length", type=int, default=4, help="Minimum string length (default: 4)")
    parser.add_argument("--filter", help="Regex or keyword to filter output")

    args = parser.parse_args()

    if not Path(args.binary).is_file():
        print("[-] File does not exist.")
        sys.exit(1)

    with open(args.binary, "rb") as f:
        data = f.read()

    ascii_strings = extract_ascii(data, args.min_length)
    utf16_strings = extract_utf16le(data, args.min_length)
    all_strings = ascii_strings + utf16_strings

    if args.filter:
        all_strings = filter_strings(all_strings, args.filter)

    for s in all_strings:
        print(s)

if __name__ == "__main__":
    main()
