import os
import argparse

def is_binary(file_path):
    # Heuristically determine if a file is binary by reading the first 1024 bytes and checking for non-text characters.
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
        return any(byte > 127 for byte in chunk)
    except Exception:
        return True  # If unreadable, assume binary

def search_keywords(file_path, keywords):
    # Searches for any of the specified keywords in the file and returns a list of matching lines with their line numbers.
    matches = []
    try:
        with open(file_path, 'r', errors='ignore') as f:
            for idx, line in enumerate(f, 1):
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        matches.append((idx, line.strip()))
                        break
    except Exception:
        pass  # Skip unreadable files
    return matches

def should_process_file(file_path, extensions, ignore_binaries):
    # Determine if a file should be processed based on extension and binary file status.
    if extensions:
        if not any(file_path.endswith(ext) for ext in extensions):
            return False
    if ignore_binaries and is_binary(file_path):
        return False
    return True

def scan_directory(path, keywords, extensions=None, ignore_binaries=False):
    # Walk through the directory tree and search files for keyword matches.
    for root, _, files in os.walk(path):
        for name in files:
            full_path = os.path.join(root, name)
            if not should_process_file(full_path, extensions, ignore_binaries):
                continue

            results = search_keywords(full_path, keywords)
            if results:
                print(f"\n[+] Matches in: {full_path}")
                for line_num, content in results:
                    print(f"  Line {line_num}: {content}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Disk Image Keyword Searcher")
    parser.add_argument("--path", required=True, help="Path to mounted disk image or folder")
    parser.add_argument("--keywords", required=True, help="Comma-separated list of keywords to search for")
    parser.add_argument("--ext", help="Optional file extensions filter (e.g., .txt,.log)")
    parser.add_argument("--ignore-binaries", action="store_true", help="Skip binary files")

    return parser.parse_args()

def main():
    args = parse_arguments()
    path = args.path
    keywords = [kw.strip() for kw in args.keywords.split(",")]
    extensions = [ext.strip() for ext in args.ext.split(",")] if args.ext else None

    print(f"[+] Starting keyword scan in: {path}")
    print(f"[+] Keywords: {', '.join(keywords)}")

    scan_directory(path, keywords, extensions, args.ignore_binaries)

if __name__ == "__main__":
    main()
