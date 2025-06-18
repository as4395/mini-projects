def decrypt_caesar(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def brute_force_caesar(ciphertext):
    print("🔍 Attempting brute-force decryption...\n")
    for shift in range(1, 26):
        candidate = decrypt_caesar(ciphertext, shift)
        print(f"[Shift {shift:2}] {candidate}")

if __name__ == "__main__":
    print("Caesar Cipher Breaker\n")
    encrypted_message = input("Enter the Caesar-encrypted message: ").strip()
    brute_force_caesar(encrypted_message)
