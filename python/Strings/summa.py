a="HeLLo"
b=''
for i in a:
    if 'a' <= i <= 'z':
        b+=chr(ord(i)-32)
    elif 'A' <= i <= 'Z':
        b+=chr(ord(i)+32)
    else:
        b+=i
print(b)