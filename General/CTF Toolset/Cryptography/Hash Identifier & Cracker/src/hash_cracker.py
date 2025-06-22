import argparse-
import hashlib
from passlib.hash import nthash

HASH_TYPES = {
    32: ['md5'],
    40: ['sha1'],
    56: ['sha224'],
    64: ['sha256'],
    96: ['sha384'],
    128: ['sha512'],
}

def identify_hash(hash_value):
    # Identify hash type based on length and known characteristics.
    length = len(hash_value)
    candidates = HASH_TYPES.get(length, [])
    if length == 32 and hash_value.islower():
        candidates.append('ntlm')
    return candidates

def compute_hash(word, hash_type):
    word_bytes = word.encode('utf-8')
    if hash_type == 'md5':
        return hashlib.md5(word_bytes).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(word_bytes).hexdigest()
    elif hash_type == 'sha224':
        return hashlib.sha224(word_bytes).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(word_bytes).hexdigest()
    elif hash_type == 'sha384':
        return hashlib.sha384(word_bytes).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(word_bytes).hexdigest()
    elif hash_type == 'ntlm':
        return nthash.hash(word)
    else:
        raise ValueError(f"Unsupported hash type: {hash_type}")

def crack_hash(target_hash, wordlist_path, hash_type):
    """Attempt to crack a hash using a wordlist and given hash type."""
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            candidate = line.strip()
            hashed = compute_hash(candidate, hash_type)
            if hashed.lower() == target_hash.lower():
                return candidate
    return None

def main():
    parser = argparse.ArgumentParser(description="Hash Identifier & Cracker")
    parser.add_argument('--hash', required=True, help="Hash value to identify or crack")
    parser.add_argument('--wordlist', required=True, help="Path to wordlist")
    parser.add_argument('--type', help="Optional hash type (e.g., md5, sha1)")

    args = parser.parse_args()
    target_hash = args.hash
    hash_type = args.type

    if not hash_type:
        guesses = identify_hash(target_hash)
        if not guesses:
            print("[-] Unable to identify hash type.")
            return
        print(f"[+] Possible hash types: {', '.join(guesses)}")
    else:
        guesses = [hash_type]

    for guess in guesses:
        print(f"[~] Trying hash type: {guess}")
        result = crack_hash(target_hash, args.wordlist, guess)
        if result:
            print(f"[+] Hash cracked! Value: {result}")
            return

    print("[-] Hash not found in wordlist.")

if __name__ == "__main__":
    main()
