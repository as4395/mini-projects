import dns.resolver
import argparse
import sys

def query_dns(domain, record_type):
    # Query DNS for a given record type.
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 3
    try:
        answers = resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []

def enumerate_subdomains(domain, subdomains):
    # Enumerate subdomains and fetch DNS records for each subdomain.
    results = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    for sub in subdomains:
        fqdn = f"{sub}.{domain}"
        records_found = {}
        for rtype in record_types:
            records = query_dns(fqdn, rtype)
            if records:
                records_found[rtype] = records
        if records_found:
            results[fqdn] = records_found
    return results

def load_wordlist(path):
    # Load subdomain wordlist from file.
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading wordlist: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="DNS Recon Tool")
    parser.add_argument("--domain", required=True, help="Target domain for enumeration")
    parser.add_argument("--wordlist", help="File containing subdomains to enumerate")

    args = parser.parse_args()

    if args.wordlist:
        subdomains = load_wordlist(args.wordlist)
    else:
        # Default common subdomains if no wordlist is provided
        subdomains = [
            "www", "mail", "ftp", "ns1", "ns2", "api", "dev", "test", "admin"
        ]

    print(f"Enumerating subdomains for: {args.domain}")

    results = enumerate_subdomains(args.domain, subdomains)

    if not results:
        print("No DNS records found for enumerated subdomains.")
        return

    for fqdn, records in results.items():
        print(f"\nSubdomain: {fqdn}")
        for rtype, vals in records.items():
            print(f"  {rtype} records:")
            for val in vals:
                print(f"    - {val}")

if __name__ == "__main__":
    main()
