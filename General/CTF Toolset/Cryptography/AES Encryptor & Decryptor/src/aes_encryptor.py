import argparse
import base64
import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
KEY_LENGTH = 32  # AES-256
IV_LENGTH = 16
PBKDF2_ITERATIONS = 100_000
SALT_SIZE = 16

def derive_key_and_iv(password: bytes, salt: bytes) -> tuple[bytes, bytes]:
    # Derive AES key and IV from password and salt using PBKDF2.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH + IV_LENGTH,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=backend,
    )
    key_iv = kdf.derive(password)
    return key_iv[:KEY_LENGTH], key_iv[KEY_LENGTH:]

def encrypt(plaintext: bytes, password: str) -> str:
    salt = os.urandom(SALT_SIZE)
    key, iv = derive_key_and_iv(password.encode(), salt)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_data = salt + ciphertext
    return base64.b64encode(encrypted_data).decode()

def decrypt(ciphertext_b64: str, password: str) -> bytes:
    encrypted_data = base64.b64decode(ciphertext_b64)
    salt = encrypted_data[:SALT_SIZE]
    ciphertext = encrypted_data[SALT_SIZE:]

    key, iv = derive_key_and_iv(password.encode(), salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

def main():
    parser = argparse.ArgumentParser(description="AES-256-CBC Encryptor/Decryptor")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encrypt', action='store_true', help='Encrypt mode')
    group.add_argument('--decrypt', action='store_true', help='Decrypt mode')

    parser.add_argument('--password', required=True, help='Password for key derivation (min 8 chars)')
    parser.add_argument('--string', help='Plaintext or base64 ciphertext string')
    parser.add_argument('--file', help='File path for input')
    parser.add_argument('--output', help='Output file path (for file input)')

    args = parser.parse_args()

    if len(args.password) < 8:
        print("Password must be at least 8 characters.")
        return

    if args.string:
        if args.encrypt:
            ciphertext = encrypt(args.string.encode(), args.password)
            print("Encrypted (base64):")
            print(ciphertext)
        else:
            try:
                plaintext = decrypt(args.string, args.password)
                print("Decrypted plaintext:")
                print(plaintext.decode())
            except Exception:
                print("Decryption failed. Check password and ciphertext.")
    elif args.file:
        if not args.output:
            print("Output file must be specified when using file input.")
            return

        with open(args.file, 'rb') as f:
            data = f.read()

        if args.encrypt:
            result = encrypt(data, args.password)
            with open(args.output, 'w') as f_out:
                f_out.write(result)
            print(f"File encrypted and saved to {args.output}")
        else:
            try:
                plaintext = decrypt(data.decode(), args.password)
                with open(args.output, 'wb') as f_out:
                    f_out.write(plaintext)
                print(f"File decrypted and saved to {args.output}")
            except Exception:
                print("Decryption failed. Check password and input file.")
    else:
        print("Either --string or --file input must be provided.")

if __name__ == "__main__":
    main()
