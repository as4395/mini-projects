# AES Encryptor/Decryptor

## Description
This command-line utility provides AES-256-CBC encryption and decryption for files and strings. 
It uses a user-supplied password to derive a secure key and IV with PBKDF2. The tool supports both encryption and decryption modes with safety checks.

## Features
- AES-256 encryption with CBC mode and PKCS7 padding
- Key and IV derived securely from a password using PBKDF2-HMAC-SHA256
- Supports encrypting/decrypting both files and plaintext strings
- Outputs base64-encoded ciphertext for easy storage and transfer

## Installation

Install dependencies:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Encrypt a string:

```bash
python aes_encryptor.py --encrypt --password mypass --string "Secret message"
```
Decrypt a string:
```bash
python aes_encryptor.py --decrypt --password mypass --string "<base64-ciphertext>"
```
Encrypt a file:
```bash
python aes_encryptor.py --encrypt --password mypass --file path/to/input.txt --output encrypted.txt
```
Decrypt a file:
```bash
python aes_encryptor.py --decrypt --password mypass --file encrypted.txt --output decrypted.txt
```

## Notes

- Password must be at least 8 characters.
- Use secure password management to avoid password reuse.
- Intended for educational and moderate security purposes.
