import string
import time
from itertools import product
from tqdm import tqdm


def dictionary_attack(password: str, wordlist: list) -> str:
    # Try to find the password in the provided wordlist.
    for word in tqdm(wordlist, desc="Dictionary Attack"):
        if word.strip() == password:
            return word
    return None


def brute_force_attack(password: str, charset: str, max_length: int) -> str:
    # Brute-force attack by generating all combinations up to max_length.
    for length in range(1, max_length + 1):
        for attempt in tqdm(product(charset, repeat=length), desc=f"Brute Force (Length {length})"):
            if ''.join(attempt) == password:
                return ''.join(attempt)
    return None


def load_wordlist(filepath: str) -> list:
    # Load words from a file into a list.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        return []


def main():
    print("=== Password Attack Challenge ===")
    password = input("Enter the password to test (will simulate cracking it): ").strip()
    print("Choose attack mode:")
    print("1. Dictionary Attack")
    print("2. Brute Force Attack")

    choice = input("Enter choice (1/2): ").strip()
    start_time = time.time()

    if choice == '1':
        wordlist_path = input("Enter path to wordlist (e.g., rockyou.txt): ").strip()
        wordlist = load_wordlist(wordlist_path)
        if not wordlist:
            return
        result = dictionary_attack(password, wordlist)

    elif choice == '2':
        charset = string.ascii_lowercase + string.digits
        try:
            max_len = int(input("Enter maximum password length to try: "))
        except ValueError:
            print("[!] Invalid input.")
            return
        result = brute_force_attack(password, charset, max_len)

    else:
        print("[!] Invalid choice.")
        return

    end_time = time.time()

    if result:
        print(f"[+] Password cracked: {result}")
    else:
        print("[-] Failed to crack the password.")

    print(f"[i] Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
