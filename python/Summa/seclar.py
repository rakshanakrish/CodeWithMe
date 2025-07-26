a=[1,2,5,3]
max=0
smax=0
for i in range(len(a)+1):
    if a[i]>a[i+1]:
        smax=max
        max=a[i]
print(max)