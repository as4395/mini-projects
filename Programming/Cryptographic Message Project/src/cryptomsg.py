import base64
import os
import sys

from Crypto.Cipher import AES, DES3, Blowfish, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import twofish

SYM_PARAMS = {
    "AES": {"key_size": 16, "block_size": AES.block_size},
    "Triple DES": {"key_size": 24, "block_size": DES3.block_size},
    "Blowfish": {"key_size": 16, "block_size": Blowfish.block_size},
    "Twofish": {"key_size": 16, "block_size": 16},
}

def generate_symmetric_key(algorithm: str) -> bytes:
    # Generate symmetric key; special parity adjustment for Triple DES
    if algorithm == "Triple DES":
        from Crypto.Cipher import DES3
        while True:
            key = os.urandom(24)
            try:
                return DES3.adjust_key_parity(key)
            except ValueError:
                continue
    return os.urandom(SYM_PARAMS[algorithm]["key_size"])

def encrypt_symmetric(algorithm: str, key: bytes, plaintext: str) -> str:
    data = plaintext.encode("utf-8")
    block_size = SYM_PARAMS[algorithm]["block_size"]

    if algorithm == "Twofish":
        cipher = twofish.Twofish(key)
        padding_len = block_size - (len(data) % block_size)
        padded = data + bytes([padding_len] * padding_len)
        ciphertext = b"".join(cipher.encrypt(padded[i:i+block_size]) for i in range(0, len(padded), block_size))
        return base64.b64encode(ciphertext).decode("utf-8")

    # For AES, Triple DES, Blowfish use CBC mode with random IV prepended
    if algorithm == "AES":
        cipher = AES.new(key, AES.MODE_CBC)
    elif algorithm == "Triple DES":
        cipher = DES3.new(key, DES3.MODE_CBC)
    elif algorithm == "Blowfish":
        cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    padded = pad(data, block_size)
    ciphertext = cipher.encrypt(padded)
    return base64.b64encode(cipher.iv + ciphertext).decode("utf-8")

def decrypt_symmetric(algorithm: str, key: bytes, ciphertext_b64: str) -> str:
    ciphertext = base64.b64decode(ciphertext_b64)
    block_size = SYM_PARAMS[algorithm]["block_size"]

    if algorithm == "Twofish":
        cipher = twofish.Twofish(key)
        decrypted = b"".join(cipher.decrypt(ciphertext[i:i+block_size]) for i in range(0, len(ciphertext), block_size))
        padding_len = decrypted[-1]
        return decrypted[:-padding_len].decode("utf-8")

    iv = ciphertext[:block_size]
    encrypted_data = ciphertext[block_size:]

    if algorithm == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif algorithm == "Triple DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
    elif algorithm == "Blowfish":
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    decrypted_padded = cipher.decrypt(encrypted_data)
    return unpad(decrypted_padded, block_size).decode("utf-8")

def generate_rsa_keypair():
    # Generate 2048-bit RSA key pair
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def encrypt_rsa(public_key_pem: bytes, plaintext: str) -> str:
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode("utf-8"))
    return base64.b64encode(ciphertext).decode("utf-8")

def decrypt_rsa(private_key_pem: bytes, ciphertext_b64: str) -> str:
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key)
    ciphertext = base64.b64decode(ciphertext_b64)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode("utf-8")

def main():
    algorithms = ["AES", "Triple DES", "Blowfish", "Twofish", "RSA"]

    print("Select an encryption algorithm:")
    for i, alg in enumerate(algorithms, 1):
        print(f"{i}. {alg}")
    choice = input("Enter choice (1-5): ").strip()

    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid choice.")
        sys.exit(1)

    algorithm = algorithms[int(choice) - 1]

    if algorithm == "RSA":
        print("\nGenerating RSA key pair...")
        priv_key, pub_key = generate_rsa_keypair()
        print("Public Key:\n", pub_key.decode())
        print("Private Key:\n", priv_key.decode())

        message = input("\nEnter message to encrypt (max ~190 chars): ")
        encrypted = encrypt_rsa(pub_key, message)
        print("\nEncrypted message:\n", encrypted)

        decrypted = decrypt_rsa(priv_key, encrypted)
        print("\nDecrypted message:\n", decrypted)

    else:
        key = generate_symmetric_key(algorithm)
        print(f"\nGenerated {algorithm} key (base64): {base64.b64encode(key).decode()}")
        message = input("Enter message to encrypt: ")
        encrypted = encrypt_symmetric(algorithm, key, message)
        print("\nEncrypted message:\n", encrypted)

        decrypted = decrypt_symmetric(algorithm, key, encrypted)
        print("\nDecrypted message:\n", decrypted)

if __name__ == "__main__":
    main()
