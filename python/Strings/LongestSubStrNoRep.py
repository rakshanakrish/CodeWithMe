a="babad"
b=set()
l,r,m,s=0,0,0,0
while(r<len(a)):
    if a[r] not in b:
        b.add(a[r])
        r+=1
        if (r-l)>m:
            m=r-l
            s=l
    else:
        b.remove(a[l])
        l+=1
        
print(a[s:s+m])
print(b)


