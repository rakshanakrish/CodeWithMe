s="aeiouae"
v="aeiou"
c=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if all(k in v for k in s[i:j]):
            c+=1
print(c)