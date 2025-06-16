n=int(input())
s=""
while n>0:
    a=n%2
    s=str(a)+s
    n=n//2
print(s)