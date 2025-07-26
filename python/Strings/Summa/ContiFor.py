phone_number="123-365-5200"
for i in phone_number:
    if i=='-':
        continue
    print(i,end="")