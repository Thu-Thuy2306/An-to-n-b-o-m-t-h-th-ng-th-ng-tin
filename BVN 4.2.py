def caesar_encrypt(plaintext, k):
    result = ""
    k = k % 26  # đưa về modulo 26
    for ch in plaintext:
        if ch.isalpha():  # chỉ mã hóa chữ cái
            base = ord('A') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - base + k) % 26 + base)
            result += new_char
        else:
            result += ch  # giữ nguyên ký tự không phải chữ
    return result

# Dữ liệu đề bài
P = "THUY"
k = 27
C = caesar_encrypt(P, k)
print("Plaintext: THUY")
print("Ciphertext:", C)
