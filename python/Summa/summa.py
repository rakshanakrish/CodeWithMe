a=[2,11,15,7]
t=9
for i in range(1,len(a)):
    if a[i-1]+a[i]==t:
        print(i-1,i)
