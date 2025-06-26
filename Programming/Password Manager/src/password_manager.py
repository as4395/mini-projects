#!/usr/bin/env python3
import os
import json
import base64
import getpass
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

STORAGE_FILE = os.path.expanduser("~/.password_manager_store.json")
SALT_SIZE = 16
NONCE_SIZE = 12

def derive_key(password: bytes, salt: bytes) -> bytes:
    # Derive a symmetric key from the password and salt using scrypt KDF."
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt(data: bytes, key: bytes) -> bytes:
    #nEncrypt data using AES-256-GCM.
    nonce = os.urandom(NONCE_SIZE)
    aesgcm = AESGCM(key)
    ct = aesgcm.encrypt(nonce, data, None)
    return nonce + ct

def decrypt(data: bytes, key: bytes) -> bytes:
    # Decrypt data using AES-256-GCM.
    nonce = data[:NONCE_SIZE]
    ct = data[NONCE_SIZE:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ct, None)

def load_storage(master_password: bytes):
    # Load and decrypt storage or create new if not exists.
    if not os.path.exists(STORAGE_FILE):
        print("[*] No existing storage found, creating new.")
        salt = os.urandom(SALT_SIZE)
        key = derive_key(master_password, salt)
        data = {}
        save_storage(data, key, salt)
        return data, key, salt

    with open(STORAGE_FILE, "rb") as f:
        file_data = f.read()

    salt = file_data[:SALT_SIZE]
    encrypted = file_data[SALT_SIZE:]
    key = derive_key(master_password, salt)

    try:
        decrypted = decrypt(encrypted, key)
        data = json.loads(decrypted.decode())
        return data, key, salt
    except Exception:
        print("[!] Incorrect master password or corrupted storage.")
        return None, None, None

def save_storage(data: dict, key: bytes, salt: bytes):
    # Encrypt and save storage to file.
    plaintext = json.dumps(data).encode()
    encrypted = encrypt(plaintext, key)
    with open(STORAGE_FILE, "wb") as f:
        f.write(salt + encrypted)

def prompt_master_password():
    return getpass.getpass("Enter master password: ").encode()

def show_menu():
    print("\nPassword Manager Menu")
    print("1) Add password")
    print("2) View password")
    print("3) Update password")
    print("4) Delete password")
    print("5) List all entries")
    print("6) Exit")

def main():
    master_password = prompt_master_password()
    storage, key, salt = load_storage(master_password)
    if storage is None:
        return

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            site = input("Enter site/app name: ").strip()
            username = input("Enter username: ").strip()
            password = getpass.getpass("Enter password: ").strip()
            storage[site] = {"username": username, "password": password}
            save_storage(storage, key, salt)
            print(f"[+] Stored password for '{site}'.")
        elif choice == "2":
            site = input("Enter site/app name to view: ").strip()
            entry = storage.get(site)
            if entry:
                print(f"Site: {site}")
                print(f"Username: {entry['username']}")
                print(f"Password: {entry['password']}")
            else:
                print(f"[!] No entry found for '{site}'.")
        elif choice == "3":
            site = input("Enter site/app name to update: ").strip()
            if site in storage:
                username = input("Enter new username: ").strip()
                password = getpass.getpass("Enter new password: ").strip()
                storage[site] = {"username": username, "password": password}
                save_storage(storage, key, salt)
                print(f"[+] Updated entry for '{site}'.")
            else:
                print(f"[!] No entry found for '{site}'.")
        elif choice == "4":
            site = input("Enter site/app name to delete: ").strip()
            if site in storage:
                del storage[site]
                save_storage(storage, key, salt)
                print(f"[+] Deleted entry for '{site}'.")
            else:
                print(f"[!] No entry found for '{site}'.")
        elif choice == "5":
            if storage:
                print("Stored entries:")
                for site in storage:
                    print(f" - {site}")
            else:
                print("[!] No stored entries.")
        elif choice == "6":
            print("Exiting password manager.")
            break
        else:
            print("[!] Invalid option, try again.")

if __name__ == "__main__":
    main()
