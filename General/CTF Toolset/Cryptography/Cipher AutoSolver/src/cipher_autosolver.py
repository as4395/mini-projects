import argparse
import string
from collections import Counter
from nltk.corpus import words
import nltk

# Ensure the word list is available
try:
    nltk.data.find("corpora/words")
except LookupError:
    nltk.download("words")

ENGLISH_WORDS = set(words.words())

def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - shift - 65) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            result.append(char)
    return ''.join(result)

def caesar_auto(text):
    for shift in range(1, 26):
        candidate = caesar_decrypt(text, shift)
        print(f"[Shift {shift}] {candidate}")

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            offset = ord(key[i % len(key)]) - ord('A')
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            decrypted = chr((ord(c) - offset - base) % 26 + base)
            plaintext.append(decrypted)
        else:
            plaintext.append(c)
    return ''.join(plaintext)

def vigenere_dictionary_attack(ciphertext, max_key_length=8):
    probable_keys = [w.upper() for w in ENGLISH_WORDS if 2 <= len(w) <= max_key_length]
    hits = []
    for key in probable_keys:
        decoded = vigenere_decrypt(ciphertext, key)
        if sum(word.lower() in ENGLISH_WORDS for word in decoded.split()) >= 2:
            hits.append((key, decoded))
    return hits

def substitution_solver(ciphertext):
    ciphertext = ciphertext.upper()
    freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    letter_counts = Counter(c for c in ciphertext if c.isalpha())
    most_common = [pair[0] for pair in letter_counts.most_common()]
    mapping = dict(zip(most_common, freq_order))

    result = ''
    for char in ciphertext:
        if char.isalpha():
            result += mapping.get(char, char).lower()
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Cipher AutoSolver Tool")
    parser.add_argument("--cipher", choices=["caesar", "vigenere", "substitution"], required=True)
    parser.add_argument("--text", required=True, help="Ciphertext input")
    parser.add_argument("--key", help="Key for vigenere (optional)")
    args = parser.parse_args()

    cipher = args.cipher
    text = args.text

    if cipher == "caesar":
        print("[*] Running Caesar brute-force...")
        caesar_auto(text)

    elif cipher == "vigenere":
        if args.key:
            print(f"[*] Using key: {args.key}")
            print(vigenere_decrypt(text, args.key))
        else:
            print("[*] Attempting dictionary attack...")
            results = vigenere_dictionary_attack(text)
            for key, decoded in results:
                print(f"[Key: {key}] {decoded}")

    elif cipher == "substitution":
        print("[*] Attempting frequency analysis...")
        result = substitution_solver(text)
        print(result)

if __name__ == "__main__":
    main()
