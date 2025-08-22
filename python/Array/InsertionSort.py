a=[1,3,4,7,6,0]
n=len(a)
for i in range(1,n):
    j=i
    while a[j-1]>a[j] and j>0:
        a[j-1],a[j]=a[j],a[j-1]
        j-=1
print(a)