s="a"
t="ab"
a=list(s)
b=[]
c=list(t)
for i in s:
    if i in t:
        b.append(i)
if a==b:
    print(True)
else:
    print(False)
print(a)
print(b)
print(c)