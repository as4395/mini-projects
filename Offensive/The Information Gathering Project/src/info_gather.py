import argparse
from dns_enum import dns_enum
from whois_lookup import whois_lookup
from subdomain_discovery import subdomain_discovery

def main(domain):
    print(f"Starting information gathering for: {domain}\n")
    
    print("1. Performing DNS enumeration...")
    dns_enum(domain)
    print("\n2. Performing WHOIS lookup...")
    whois_lookup(domain)
    print("\n3. Discovering subdomains...")
    subdomain_discovery(domain)
    print("\nInformation gathering complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Information Gathering Tool")
    parser.add_argument("--domain", required=True, help="Target domain for reconnaissance")
    args = parser.parse_args()
    main(args.domain)
