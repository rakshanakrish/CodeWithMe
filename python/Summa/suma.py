a=[2,2,0,4,0,8]
for i in range(1,len(a)):
    if a[i-1]==a[i] and a[i]>0 and a[i-1]>0:
        a[i-1]=a[i-1]*2
        a[i]=0
b=[]
c=[]
for i in range(len(a)):
    if a[i]!=0:
        b.append(a[i])
for i in range(len(a)):
    if a[i]==0:
        c.append(a[i])
print(b+c)
