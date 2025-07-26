B = 12
N = 1720
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

if N == 0:
    print("0")

while N > 0:
    remainder = N % B
    result = chars[remainder] + result
    N //= B
    print(N)
print(chars[remainder])
print(result)
