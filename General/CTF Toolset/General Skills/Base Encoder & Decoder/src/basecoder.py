import argparse
import base64
import sys

def encode_all(input_str: str):
    # Encode the string in various base formats
    raw = input_str.encode()
    print("[*] Encoding Results:")
    print("Base16 :", base64.b16encode(raw).decode())
    print("Base32 :", base64.b32encode(raw).decode())
    print("Base64 :", base64.b64encode(raw).decode())
    print("Base85 :", base64.b85encode(raw).decode())

def try_decode(input_str: str):
    # Attempt to decode the input string with multiple bases
    for name, decoder in [
        ("Base16", base64.b16decode),
        ("Base32", base64.b32decode),
        ("Base64", base64.b64decode),
        ("Base85", base64.b85decode)
    ]:
        try:
            padded = input_str + '=' * (-len(input_str) % 4)
            decoded = decoder(padded.encode()).decode('utf-8')
            print(f"[+] {name} decoded: {decoded}")
        except Exception:
            continue
    print("[-] If nothing decoded correctly, try another tool or method.")

def main():
    parser = argparse.ArgumentParser(description="Base Encoder/Decoder")
    parser.add_argument("--encode", help="String to encode into multiple base formats")
    parser.add_argument("--decode", help="Base-encoded string to decode")

    args = parser.parse_args()

    if args.encode:
        encode_all(args.encode)
    elif args.decode:
        try_decode(args.decode)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
