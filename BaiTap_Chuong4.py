def caesar_encrypt(plaintext, k):
    result = ""
    k = k % 26
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char
    return result

plaintext = "Thuy"
k = 27
ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
