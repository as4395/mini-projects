import requests
from typing import List
import time

BLOCKLIST_URLS = [
    # Ads
    "https://easylist.to/easylist/easylist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
    # Privacy
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
    # Malware
    "https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-online.txt",
    "https://malware-filter.gitlab.io/malware-filter/phishing-filter.txt",
    # Regional example
    "https://easylist.to/easylistgermany/easylistgermany.txt",
]

OUTPUT_FILE = "adblock_domains.txt"


def fetch_blocklist(url: str) -> List[str]:
    """Fetches the blocklist from a URL and returns lines."""
    try:
        print(f"Downloading blocklist from {url} ...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        content = response.text
        lines = content.splitlines()
        return lines
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []


def parse_domains(lines: List[str]) -> List[str]:
    """
    Parse domain names from blocklist lines.
    This handles common blocklist formats (hosts file style, adblock filter style).
    """
    domains = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Hosts file format: "0.0.0.0 domain.com"
        if line.startswith("0.0.0.0 ") or line.startswith("127.0.0.1 "):
            parts = line.split()
            if len(parts) >= 2:
                domains.add(parts[1].lower())
        # Adblock filter format: "||domain.com^"
        elif line.startswith("||") and line.endswith("^"):
            domain = line[2:-1]
            if domain:
                domains.add(domain.lower())
        # Plain domain lines
        elif all(c.isalnum() or c in "-." for c in line):
            domains.add(line.lower())
    return list(domains)


def update_blocklist():
    all_domains = set()
    for url in BLOCKLIST_URLS:
        lines = fetch_blocklist(url)
        domains = parse_domains(lines)
        print(f"Fetched {len(domains)} domains from {url}")
        all_domains.update(domains)

    print(f"Total unique domains aggregated: {len(all_domains)}")

    with open(OUTPUT_FILE, "w") as f:
        for domain in sorted(all_domains):
            f.write(domain + "\n")

    print(f"Blocklist updated and saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    update_blocklist()
