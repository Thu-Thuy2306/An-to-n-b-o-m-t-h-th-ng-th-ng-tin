import math

# step 1: chọn số nguyên tố
p = 17
q = 23

# step 2: tính n
n = p * q
print("n =", n)

# step 3: tính phi(n)
phi = (p - 1) * (q - 1)
print("phi =", phi)

# step 4: chọn e (cho trước)
e = 5
if math.gcd(e, phi) != 1:
    raise ValueError("e không hợp lệ")
print("e =", e)

# step 5: tìm d (nghịch đảo modular của e theo phi)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

d = mod_inverse(e, phi)
print("d =", d)
print(f'Public key: {(e, n)}')
print(f'Private key: {(d, n)}')

# step 6: thông điệp
message = "THUY"
print("Original message:", message)

# step 7: mã hóa từng ký tự
encrypted = []
for char in message:
    m = ord(char)  # mã ASCII
    c = pow(m, e, n)
    encrypted.append(c)
print("Encrypted:", encrypted)

# step 8: giải mã
decrypted = ""
for c in encrypted:
    m = pow(c, d, n)
    decrypted += chr(m)
print("Decrypted:", decrypted)
