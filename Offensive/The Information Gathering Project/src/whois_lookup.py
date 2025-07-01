import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print("WHOIS Information:")
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"WHOIS lookup failed: {e}")
