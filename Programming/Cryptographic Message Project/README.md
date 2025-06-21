# Cryptographic Message Project

## Description
A versatile tool for encrypting and decrypting string messages using popular cryptographic algorithms. It supports symmetric algorithms (AES, Triple DES, Blowfish, Twofish), asymmetric RSA encryption, 
and is designed for secure communication demonstration and practical cryptographic learning purposes.

## Features
- Symmetric encryption and decryption with AES, Triple DES, Blowfish, and Twofish
- RSA public/private key pair generation and asymmetric encryption
- Secure key generation and handling
- Uses CBC mode with a random initalization vector for symmetric algorithms (except Twofish uses ECB due to library constraints)
- PKCS1_OAEP padding for RSA encryption
- Clear CLI interface for selecting algorithms and operations

## Installation
Install required dependencies via:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Run from the ```src``` directory:

```bash
python cryptomsg.py
```
Follow the prompts to choose an algorithm, encrypt and decrypt messages.

## Notes

- RSA encryption is only suitable only for short messages due to key size limitations.
- Twofish uses ECB mode for demonstration, which is not recommended for sensitive data.
- For real-world applications, enhance key storage, authentication, and use secure channels.
