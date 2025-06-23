import requests
import concurrent.futures
import sys
from typing import List

# List of platforms to check (extendable)
PLATFORMS = {
    "Facebook":       "https://www.facebook.com/{}",
    "Instagram":      "https://www.instagram.com/{}",
    "X (Twitter)":    "https://x.com/{}",
    "Reddit":         "https://www.reddit.com/user/{}",
    "TikTok":         "https://www.tiktok.com/@{}",
    "Snapchat":       "https://www.snapchat.com/add/{}",
    "LinkedIn":       "https://www.linkedin.com/in/{}",
    "YouTube":        "https://www.youtube.com/{}",
    "Pinterest":      "https://www.pinterest.com/{}",
    "Tumblr":         "https://{}.tumblr.com",
    "SoundCloud":     "https://soundcloud.com/{}",
    "Spotify":        "https://open.spotify.com/user/{}",
    "Twitch":         "https://www.twitch.tv/{}",
    "GitHub":         "https://github.com/{}",
    "Medium":         "https://medium.com/@{}",
    "Venmo":          "https://venmo.com/{}",
    "CashApp":        "https://cash.app/${}",
    "Gravatar":       "https://en.gravatar.com/{}",
    "Flickr":         "https://www.flickr.com/people/{}",
    "DeviantArt":     "https://www.deviantart.com/{}",
    "Imgur":          "https://imgur.com/user/{}",
    "Roblox":         "https://www.roblox.com/users/profile?username={}",
    "Replit":         "https://replit.com/@{}",
    "Archive.org":    "https://archive.org/details/@{}",
    "TripAdvisor":    "https://www.tripadvisor.com/Profile/{}",
    "Letterboxd":     "https://letterboxd.com/{}",
    "Steam":          "https://steamcommunity.com/id/{}",
    "HackerRank":     "https://www.hackerrank.com/{}",
    "LeetCode":       "https://leetcode.com/{}",
    "Pastebin":       "https://pastebin.com/u/{}",
    "OK.ru":          "https://ok.ru/{}",
    "VK":             "https://vk.com/{}",
    "Pornhub":        "https://www.pornhub.com/users/{}",
    "OnlyFans":       "https://onlyfans.com/{}",
    "MyAnimeList":    "https://myanimelist.net/profile/{}",
    "Anilist":        "https://anilist.co/user/{}",
    "Keybase":        "https://keybase.io/{}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; UsernameProfiler/1.0)"
}

def check_username(site: str, url_template: str, username: str) -> str:
    # Format URL and check for HTTP 200 response.
    url = url_template.format(username)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=5)
        if resp.status_code == 200:
            return f"[+] {site}: FOUND at {url}"
        elif resp.status_code == 404:
            return f"[-] {site}: Not found"
        else:
            return f"[?] {site}: Unexpected status code {resp.status_code}"
    except requests.RequestException as e:
        return f"[!] {site}: Error - {e}"

def run_checks(username: str):
    """Run all checks in parallel."""
    print(f"\n[•] Checking presence of username: {username}\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(check_username, site, url, username)
            for site, url in PLATFORMS.items()
        ]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <username>")
        sys.exit(1)

    username = sys.argv[1].strip()
    if not username:
        print("Username cannot be empty.")
        sys.exit(1)

    run_checks(username)

if __name__ == "__main__":
    main()
