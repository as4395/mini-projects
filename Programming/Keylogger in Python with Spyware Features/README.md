# Keylogger with Spyware Features

## Description
This project implements a Python-based keylogger with basic spyware features for educational use in a controlled lab environment. It captures keyboard input, clipboard content, periodic screenshots, and system information, and logs them to a secure file for later analysis. This tool helps understand how malicious monitoring software works, and how to defend against it.

## Features
- Logs all keystrokes to a local file
- Captures clipboard data
- Takes periodic desktop screenshots
- Collects basic system information (hostname, OS, IP, etc.)
- Simple modular design for extending to email exfiltration or remote control

## Installation
Install the required packages with:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Run the keylogger script from the `src/` directory:

```bash
cd src/
python keylogger.py
```

Logs will be saved to `logs/` and screenshots to `screenshots/`.

## Notes
- This tool uses `pynput` for key capture, `pyperclip` for clipboard access, `Pillow` for screenshots, and `platform/socket` for system info.
- Log files and captured screenshots are stored locally unless extended to send remotely.
- This implementation is for learning purposes only and demonstrates how spyware components are structured.
- Use this tool **only** in authorized test environments. Do **not** deploy on machines or networks without consent.
