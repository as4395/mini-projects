# The Injections Project

This project explores and automates various web injection attacks, such as SQL Injection, Command Injection, and Cross-Site Scripting (XSS), against intentionally vulnerable applications for educational and penetration testing purposes.

## Features

- SQL Injection (Error-based, Boolean-based, Time-based)
- Command Injection (Basic testing via shell commands)
- Reflected XSS detection
- Basic reporting of vulnerabilities
- Target configurable via CLI

## Usage

```bash
python3 src/injection_tester.py --url http://example.com/vuln.php?id=1 --technique sql
```

## Techniques

| Technique | Description                          |
|----------|--------------------------------------|
| `sql`    | Performs basic SQL Injection checks  |
| `xss`    | Tests for reflected XSS              |
| `cmd`    | Checks for simple command injection  |

## Requirements

- Python 3+
- Requests
- BeautifulSoup4

Install dependencies:

```bash
pip install -r requirements.txt
```

## Example

```bash
python3 src/injection_tester.py --url http://testphp.vulnweb.com/artists.php?artist=1 --technique sql
```

**Warning:** This tool is for educational purposes only. Use only on systems you own or have explicit permission to test.
