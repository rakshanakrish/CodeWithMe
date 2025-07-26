n=4
a=[43,345,20,987]
b=[]
for i in a:
    bb=str(i)
    c=0
    for j in bb:
        c+=int(j)
    b.append(c)
print(b)