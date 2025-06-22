# Cipher AutoSolver

## Description
A command-line tool that detects and attempts to automatically solve classical ciphers often seen in CTFs, including Caesar, Vigenère, and monoalphabetic substitution ciphers. It is designed for quick decoding of plaintext or hints embedded in challenge data.

## Features
- Detects Caesar, Vigenère, and monoalphabetic substitution ciphers
- Automatically brute-forces Caesar shifts
- Supports known-key and dictionary-based Vigenère decryption
- Substitution solver using frequency analysis and pattern matching
- Clean CLI interface with selectable modes

## Installation

Install dependencies using:

```bash
pip install -r requirements/requirements.txt
```

## Usage

```bash
python cipher_autosolver.py --cipher caesar --text "KHOOR ZRUOG"
```
```bash
python cipher_autosolver.py --cipher vigenere --text "LXFOPVEFRNHR" --key "LEMON"
````
```bash
python cipher_autosolver.py --cipher substitution --text "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
```

## Notes

- Substitution cracking is assisted using English letter frequency heuristics.
- Caesar mode runs all 25 possible shifts unless a specific one is given.
- Vigenère mode supports both known-key and brute-force dictionary attack.
- Useful for solving intro-level CTF crypto puzzles.
