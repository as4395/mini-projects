# Reverse Shell Generator Tool

## Description
This tool dynamically generates reverse shell payload scripts in multiple languages based on user-provided parameters including target IP address, listening port, and desired payload language (e.g., Python, Bash, PHP).  
It helps automate creating payloads for penetration testing or learning reverse shell concepts.

## Features
- Generate reverse shell payloads for popular languages: Python, Bash, PHP, Netcat
- Accepts user input for IP address and port
- Outputs ready-to-use script or one-liner payload
- Lightweight and command-line based

## Installation
No external libraries required. Requires Python 3 to run the generator script.

## Usage

Run the generator script:

```bash
python reverse_shell_generator.py
```

Follow the prompts to input:

- Target IP address
- Listening port
- Payload language (Python, Bash, PHP, Netcat)
- The tool outputs the generated payload script or one-liner.

## Notes

- This tool is intended for educational and authorized use only.
- Generated payloads must be used in a controlled environment.
- Make sure to start a listener on the specified IP and port before deploying payloads.
