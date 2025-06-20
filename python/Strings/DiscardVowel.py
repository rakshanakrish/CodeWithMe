## Removing vowels
s='rAkshana'
a=list(s.lower())
b=['a','e','i','o','u']
for i in a :
    for j in (b):
        if j in i:
            a.remove(j)
print(a)