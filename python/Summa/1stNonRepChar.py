a="aabbcde"
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        b.clear()
print(*b[0])
