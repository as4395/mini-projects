# Custom Disassembler Wrapper

## Description
This tool provides a user-friendly CLI interface for disassembling binary code using the Capstone disassembly engine. It allows users to input raw bytes from a binary file or hexadecimal string and outputs readable assembly instructions. It supports multiple architectures and modes (e.g., x86 32-bit, x86 64-bit, ARM).

---

## Features
- Disassemble raw binary code from files or hex strings
- Supports multiple architectures: x86, x64, ARM, ARM64
- Selectable architecture and mode at runtime
- CLI interface for easy usage and scripting

---

## Installation

Install the required package with:

```bash
pip install -r requirements/requirements.txt
```

---

## Usage

### Disassemble a hex string:
```bash
python disasm_wrapper.py --hex "b800000000c3" --arch x86 --mode 32
```

### Disassemble a binary file:
```bash
python disasm_wrapper.py --file shellcode.bin --arch x86 --mode 64
```

Supported architectures: `x86`, `x64`, `arm`, `arm64`  
#
### Modes:  
- For `x86`: use `32` or `64`  
- For `arm`: use `arm` or `thumb`  
- For `arm64`: no mode needed

---

## Notes

- Ensure shellcode files are raw binary (not hex).
- Only common Capstone architectures and modes are supported.
- Designed for RE-based CTF challenges.
