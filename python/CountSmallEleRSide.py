a=[12,1,2,3,0,11,4]
b=[0]*len(a)
for i in range(len(a)):
    count=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            count+=1
    b[i]=count
print(b)


