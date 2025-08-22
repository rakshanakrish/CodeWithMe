a,b=11,25
s=[]
for n in range(a,b+1):
  if n>1:
    ip=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
           ip=False
           break
    if ip:
       s.append(n)
print(s)