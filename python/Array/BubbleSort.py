a=[1,3,4,7,6,0]
n=len(a)
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            swapped=True
    #By using swapped we can avoid unnecessay loop
    if not swapped:
        break
print(a)