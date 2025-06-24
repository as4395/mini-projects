# Email Verifier

## Description
This tool verifies the existence and validity of an email address by checking its domain's DNS MX records and optionally querying the SMTP server to verify the recipient address.

## Features
- Checks if the email domain has valid MX records
- Attempts SMTP verification by issuing RCPT TO command
- Basic validation of email format
- Lightweight and fast for quick verification

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Usage

Run the verifier with an email address:
```bash
python email_verifier.py user@example.com
```
Optional argument to specify the sender email (used during SMTP handshake):
```bash
python email_verifier.py user@example.com --from-email sender@example.com
```

## Notes

- SMTP verification depends on the target server's policies; some servers disable or block such checks.
- This tool does not guarantee 100% accuracy but is a useful heuristic.
- Use responsibly and ethically.
