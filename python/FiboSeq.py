n=10
a=0
b=1
c=0
d=[0,1]
while c<=n:
    e=a+b
    d.append(e)
    c+=1
    a,b=b,e
print(*d)
