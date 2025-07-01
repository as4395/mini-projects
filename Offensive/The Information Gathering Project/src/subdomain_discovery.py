import requests

COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "webmail", "ns1", "ns2", "blog", "shop", "dev", "test"
]

def subdomain_discovery(domain):
    print(f"Checking common subdomains for {domain}:")
    for sub in COMMON_SUBDOMAINS:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400:
                print(f"Found subdomain: {sub}.{domain} (Status: {r.status_code})")
        except requests.RequestException:
            continue
