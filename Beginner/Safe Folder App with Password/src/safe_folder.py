import os
import sys
import getpass
import base64
import json
from pathlib import Path
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

# Directory where encrypted files are stored
SAFE_DATA_DIR = Path(__file__).parent.parent / "safe_data"

# Configuration file storing salt and password verification token
CONFIG_FILE = Path(__file__).parent.parent / "config.json"

# Constants for key derivation
SALT_SIZE = 16
ITERATIONS = 100_000

# Backend cryptographic provider
backend = default_backend()


def create_salt():
    """Generate a random salt for key derivation."""
    return os.urandom(SALT_SIZE)


def load_config():
    """Load stored configuration (salt and verification token) from file."""
    if not CONFIG_FILE.exists():
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    """Save configuration (salt and verification token) to file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def derive_key(password: bytes, salt: bytes) -> bytes:
    """
    Derive a symmetric encryption key from the password and salt
    using PBKDF2-HMAC-SHA256 with configured iterations.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
        backend=backend,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def initialize():
    """
    Initialize the app: load config and verify master password,
    or prompt user to create one if none exists.
    Returns the derived key on success, or exits on failure.
    """
    config = load_config()
    if config is None:
        print("No master password set. Please create one.")
        while True:
            pwd1 = getpass.getpass("Enter new master password: ")
            pwd2 = getpass.getpass("Confirm master password: ")
            if pwd1 != pwd2:
                print("Passwords do not match. Try again.")
            elif len(pwd1) < 8:
                print("Password must be at least 8 characters. Try again.")
            else:
                break
        salt = create_salt()
        key = derive_key(pwd1.encode(), salt)
        # Encrypt a verification token to validate password correctness later
        verification_token = Fernet(key).encrypt(b"verify_password")
        config = {
            "salt": base64.b64encode(salt).decode(),
            "verification": verification_token.decode(),
        }
        save_config(config)
        print("Master password set successfully.")
    else:
        # Prompt for password up to 3 times and verify
        for _ in range(3):
            pwd = getpass.getpass("Enter master password: ")
            salt = base64.b64decode(config["salt"])
            key = derive_key(pwd.encode(), salt)
            fernet = Fernet(key)
            try:
                fernet.decrypt(config["verification"].encode())
                print("Access granted.")
                return key
            except InvalidToken:
                print("Incorrect password.")
        print("Too many failed attempts. Exiting.")
        sys.exit(1)
    return key


def list_files():
    """List all files currently stored in the safe folder."""
    SAFE_DATA_DIR.mkdir(exist_ok=True)
    files = [f.name for f in SAFE_DATA_DIR.iterdir() if f.is_file()]
    if not files:
        print("No files in safe folder.")
    else:
        print("Files in safe folder:")
        for i, filename in enumerate(files, 1):
            print(f"  {i}. {filename}")


def encrypt_file(key, filepath):
    """
    Encrypt a file from the given path and save the encrypted version
    in the safe folder. Avoids overwriting existing safe files.
    """
    SAFE_DATA_DIR.mkdir(exist_ok=True)
    path = Path(filepath)
    if not path.is_file():
        print(f"File '{filepath}' does not exist or is not a file.")
        return
    dest_path = SAFE_DATA_DIR / path.name
    if dest_path.exists():
        print(f"File '{path.name}' already exists in safe folder.")
        return

    with open(filepath, "rb") as f:
        data = f.read()
    encrypted = Fernet(key).encrypt(data)
    with open(dest_path, "wb") as f:
        f.write(encrypted)
    print(f"File '{path.name}' encrypted and added to safe folder.")


def decrypt_file(key, filename):
    """
    Decrypt and display the contents of a file in the safe folder.
    Handles errors for corrupted files or wrong password.
    """
    path = SAFE_DATA_DIR / filename
    if not path.exists():
        print(f"File '{filename}' not found in safe folder.")
        return

    with open(path, "rb") as f:
        encrypted_data = f.read()
    try:
        decrypted = Fernet(key).decrypt(encrypted_data)
    except InvalidToken:
        print("Decryption failed. Wrong password or corrupted file.")
        return

    print(f"\nContents of '{filename}':\n")
    try:
        print(decrypted.decode("utf-8"))
    except UnicodeDecodeError:
        print("[Binary data cannot be displayed]")


def delete_file(filename):
    """Delete a specified file from the safe folder."""
    path = SAFE_DATA_DIR / filename
    if not path.exists():
        print(f"File '{filename}' not found in safe folder.")
        return
    path.unlink()
    print(f"File '{filename}' deleted from safe folder.")


def main():
    """Main application loop presenting options to the user."""
    key = initialize()
    while True:
        print("\nOptions:")
        print("1. List files")
        print("2. Add file to safe folder")
        print("3. View file contents")
        print("4. Delete file")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            list_files()
        elif choice == "2":
            filepath = input("Enter path to file to add: ").strip()
            encrypt_file(key, filepath)
        elif choice == "3":
            filename = input("Enter filename to view: ").strip()
            decrypt_file(key, filename)
        elif choice == "4":
            filename = input("Enter filename to delete: ").strip()
            delete_file(filename)
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
