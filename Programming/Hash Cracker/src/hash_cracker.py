import hashlib
from tqdm import tqdm
import os

# Mapping hash length to possible algorithms
def detect_hash_type(hash_value):
    length = len(hash_value)
    return {
        32: 'md5',
        40: 'sha1',
        64: 'sha256',
        128: 'sha512'
    }.get(length, None)


def hash_word(word, algo):
    encoded = word.encode()
    if algo == 'md5':
        return hashlib.md5(encoded).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(encoded).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(encoded).hexdigest()
    elif algo == 'sha512':
        return hashlib.sha512(encoded).hexdigest()
    else:
        raise ValueError(f"Unsupported hash algorithm: {algo}")


def crack_hash(target_hash, wordlist_path, algo=None, log_results=False):
    if not algo:
        algo = detect_hash_type(target_hash)
        if not algo:
            print("Unable to detect hash algorithm. Please specify manually.")
            return
        else:
            print(f"Detected hash type: {algo.upper()}")

    if not os.path.exists(wordlist_path):
        print("Wordlist file not found.")
        return

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        words = f.readlines()

    print("Starting brute-force attack...\n")
    for word in tqdm(words, desc="Cracking", unit="word"):
        word = word.strip()
        if not word:
            continue

        hashed = hash_word(word, algo)
        if hashed == target_hash:
            print(f"\nMatch found!\nHash: {target_hash}\nWord: {word}")
            if log_results:
                with open("cracked_hashes.txt", "a") as log:
                    log.write(f"{target_hash} : {word}\n")
            return

    print("\nNo match found in the wordlist.")


if __name__ == '__main__':
    print("Advanced Hash Cracker\n")
    target = input("Enter the hash to crack: ").strip()
    wordlist = input("Enter path to the wordlist file: ").strip()
    algo_input = input("Enter hash algorithm (leave blank to auto-detect): ").strip().lower() or None
    log_choice = input("Log results to file if cracked? (y/n): ").strip().lower()
    log_enabled = log_choice == 'y'

    crack_hash(target, wordlist, algo_input, log_results=log_enabled)
