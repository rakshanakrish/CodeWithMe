n=int(input())
b=[]
for i in range(1,n+1):
    a=i*(i+1)//2
    b.append(a)
    if a>=n:
        break

if n in b:
    print("Triangular Number")
else:
    print("Not a Triangular Number")

