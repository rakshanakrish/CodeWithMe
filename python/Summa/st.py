n=int(input())
a=0
b=1
c=[0,1]
for i in range(2,n+1):
    d=a+b
    a=b
    b=d
    c.append(d)
print(*c)
    