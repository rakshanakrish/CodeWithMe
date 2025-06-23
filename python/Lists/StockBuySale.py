a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            c=a[j]-a[i]
            if b<c:
                b=c
print(b)
#a=[7, 10, 1, 3, 6, 9, 2]


