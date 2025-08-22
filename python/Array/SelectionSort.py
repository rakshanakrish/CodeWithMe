a=[1,3,4,7,6,0]
n=len(a)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if a[j]<a[min_index]:
            min_index=j
    #The below technique is to pop and insert into the respective place
    '''min_val=a.pop(min_index)
    a.insert(i,min_val)'''
    #or
    #optimized way of swaping
    a[i],a[min_index]=a[min_index],a[i]
print(a)