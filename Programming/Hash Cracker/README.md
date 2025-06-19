# Advanced Hash Cracker

## Description
This is a Python-based hash cracking utility. It supports cracking hashes using dictionary attacks and is compatible with common algorithms like MD5, SHA-1, SHA-256, and SHA-512. The tool also supports auto-detection of the hash type based on its length.
It is built for learning purposes and for testing the effectiveness of passwords and hash protections.

---

## Features

- Dictionary-based hash cracking
- Supports MD5, SHA-1, SHA-256, and SHA-512
- Automatically detects the hash algorithm based on length
- Displays a progress bar while processing
- Optionally logs successful cracks to a file
- Modular and extensible Python code

---

## Usage

1. Navigate to the `src/` folder.
2. Run the script:

```bash
python3 hash_cracker.py
```

3. Follow the prompts:
   - Enter the hash to crack
   - Provide the path to your wordlist file
   - Choose the hash algorithm (or press Enter to auto-detect)
   - Choose whether to log successful results

---

## Example

Input:
```
Enter the hash to crack: e10adc3949ba59abbe56e057f20f883e
Enter path to the wordlist file: rockyou.txt
Enter hash algorithm (leave blank to auto-detect):
Log results to file if cracked? (y/n): y
```

Output:
```
Match found!
Hash: e10adc3949ba59abbe56e057f20f883e
Word: 123456
```

---

## Requirements

- Python 3
- tqdm

Install required libraries using:

```bash
pip install -r requirements.txt
```
