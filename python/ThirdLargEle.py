## Find 3rd largest element
a=[4,5,8,7,6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a[-3])

# Another method

#a=[4,5,8,7,6]
#a.sort()
#print(a[-3])
