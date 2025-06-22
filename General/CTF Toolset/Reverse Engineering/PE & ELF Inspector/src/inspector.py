import sys
import lief
import argparse
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output (cross-platform)
init(autoreset=True)

def detect_format(file_path):
    # Detects binary format by reading magic bytes and returns 'PE', 'ELF', or 'Unknown'.
  
    with open(file_path, 'rb') as f:
        magic = f.read(4)
        if magic.startswith(b'MZ'):
            return 'PE'
        elif magic.startswith(b'\x7fELF'):
            return 'ELF'
        else:
            return 'Unknown'

def inspect_elf(binary):
    # Displays ELF binary metadata, sections, and symbols.
    print(f"{Fore.CYAN}ELF Binary Detected")
    print(f"{Fore.YELLOW}Architecture: {binary.header.machine_type.name}")
    print(f"Entry Point: {hex(binary.header.entrypoint)}\n")

    print(f"{Fore.GREEN}Sections:")
    for section in binary.sections:
        print(f"  - {section.name} | Size: {section.size} bytes | Offset: {hex(section.offset)}")

    if binary.has_symbols:
        print(f"\n{Fore.MAGENTA}Symbols:")
        for symbol in binary.symbols[:10]:  # Show first 10 symbols
            print(f"  - {symbol.name} @ {hex(symbol.value)}")

def inspect_pe(binary):
    # Displays PE binary metadata, sections, and imported libraries.
    print(f"{Fore.CYAN}PE Binary Detected")
    print(f"{Fore.YELLOW}Architecture: {binary.header.machine.name}")
    print(f"Entry Point: {hex(binary.optional_header.addressof_entrypoint)}\n")

    print(f"{Fore.GREEN}Sections:")
    for section in binary.sections:
        print(f"  - {section.name} | Virtual Size: {section.virtual_size} | Raw Size: {section.size}")

    if binary.has_imports:
        print(f"\n{Fore.MAGENTA}Imported Libraries:")
        for lib in binary.imports:
            print(f"  - {lib.name}")

def main():
    parser = argparse.ArgumentParser(description="PE/ELF Binary Inspector")
    parser.add_argument("file", help="Path to binary file")
    args = parser.parse_args()

    file_path = args.file
    fmt = detect_format(file_path)

    if fmt == 'Unknown':
        print(f"{Fore.RED}Unsupported or unknown file format.")
        sys.exit(1)

    try:
        binary = lief.parse(file_path)
    except Exception as e:
        print(f"{Fore.RED}Failed to parse binary: {e}")
        sys.exit(1)

    # Delegate inspection based on detected format
    if fmt == 'PE':
        inspect_pe(binary)
    elif fmt == 'ELF':
        inspect_elf(binary)

if __name__ == "__main__":
    main()
