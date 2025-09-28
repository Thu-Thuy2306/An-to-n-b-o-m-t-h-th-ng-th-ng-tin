# RSA Demo với p=17, q=23, e=5
def egcd(a, b):
    """Thuật toán Euclid mở rộng"""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def mod_inverse(e, phi):
    """Tìm nghịch đảo modulo"""
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo modular")
    return x % phi

# ===== Bước 1: Khởi tạo =====
p = 17
q = 23
e = 5
n = p * q
phi = (p - 1) * (q - 1)

# ===== Bước 2: Tính khóa =====
d = mod_inverse(e, phi)
print(f"Khóa công khai: (e={e}, n={n})")
print(f"Khóa bí mật: (d={d}, n={n})")

# ===== Bước 3: Chuẩn bị thông điệp =====
plaintext = "THUY"
plaintext_nums = [ord(ch) for ch in plaintext]
print("Bản rõ (ASCII):", plaintext_nums)

# ===== Bước 4: Mã hóa =====
ciphertext = [pow(m, e, n) for m in plaintext_nums]
print("Bản mã:", ciphertext)

# ===== Bước 5: Giải mã =====
decrypted_nums = [pow(c, d, n) for c in ciphertext]
decrypted_text = ''.join(chr(m) for m in decrypted_nums)
print("Giải mã (ASCII):", decrypted_nums)
print("Thông điệp gốc:", decrypted_text)
