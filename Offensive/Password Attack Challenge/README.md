# Password Attack Challenge

This project simulates a password brute-force attack to test the strength of various passwords. It allows users to define a list of passwords of varying complexity and attempts to crack them using a wordlist or brute-force method.
This tool is meant strictly for educational purposes to demonstrate the importance of secure passwords.

## Features

- Offline brute-force simulation (no network attack)
- Supports dictionary-based and character-set brute-force attacks
- Tests password strength based on complexity and time to crack

## Usage

**1.** Install dependencies (optional):
```bash
pip install -r requirements.txt
```
2. Run the program:
```bash
python3 src/password_attack.py
```
3. Choose attack mode (dictionary or brute-force), input the target password or file, and analyze results.

## Notes

- For brute-force mode, limit password length or use it for short passwords only.
- A real attack should never be carried out on live systems without authorization.
