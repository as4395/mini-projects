import argparse
import binascii
import sys

from capstone import *

ARCH_MAP = {
    'x86': CS_ARCH_X86,
    'x64': CS_ARCH_X86,
    'arm': CS_ARCH_ARM,
    'arm64': CS_ARCH_ARM64,
}

MODE_MAP = {
    'x86': {'32': CS_MODE_32, '64': CS_MODE_64},
    'x64': {'64': CS_MODE_64},
    'arm': {'arm': CS_MODE_ARM, 'thumb': CS_MODE_THUMB},
    'arm64': {'': CS_MODE_ARM},  # Default, required for capstone API
}

def load_bytes_from_file(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception as e:
        print(f"[-] Failed to read file: {e}")
        sys.exit(1)

def parse_hex_string(hex_str):
    try:
        return binascii.unhexlify(hex_str)
    except binascii.Error:
        print("[-] Invalid hex string.")
        sys.exit(1)

def disassemble(code_bytes, arch, mode):
    disassembler = Cs(ARCH_MAP[arch], mode)
    disassembler.detail = True

    for instr in disassembler.disasm(code_bytes, 0x1000):
        print(f"0x{instr.address:x}:\t{instr.mnemonic}\t{instr.op_str}")

def main():
    parser = argparse.ArgumentParser(description="Custom Disassembler Wrapper (Capstone-based)")
    parser.add_argument("--hex", help="Hex string of instructions to disassemble")
    parser.add_argument("--file", help="Path to binary file containing raw instructions")
    parser.add_argument("--arch", required=True, choices=["x86", "x64", "arm", "arm64"], help="Architecture")
    parser.add_argument("--mode", required=False, help="Disassembly mode (e.g., 32, 64, arm, thumb)")

    args = parser.parse_args()

    if not args.hex and not args.file:
        print("[-] You must provide either --hex or --file")
        sys.exit(1)

    arch = args.arch
    arch_modes = MODE_MAP[arch]

    if arch == "arm64":
        mode = CS_MODE_ARM  # Capstone requires a default even though the mode is implicit
    else:
        if not args.mode or args.mode not in arch_modes:
            print(f"[-] Invalid or missing mode for architecture '{arch}'. Valid modes: {list(arch_modes)}")
            sys.exit(1)
        mode = arch_modes[args.mode]

    if args.hex:
        code_bytes = parse_hex_string(args.hex)
    else:
        code_bytes = load_bytes_from_file(args.file)

    print(f"[+] Disassembling {len(code_bytes)} bytes...")
    disassemble(code_bytes, arch, mode)

if __name__ == "__main__":
    main()
