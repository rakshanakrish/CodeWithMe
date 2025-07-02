a="cddab"
m=""
for i in range(len(a)):
    #odd position
    l=r=i
    while l>=0 and r<len(a) and a[l]==a[r]:
        if (r-l+1)>len(m):
            m=a[l:r+1]
        l-=1
        r+=1
    #even position
    l,r=i,i+1
    while l>=0 and r<len(a) and a[l]==a[r]:
        if (r-l+1)>len(m):
            m=a[l:r+1]
        l-=1
        r+=1
print(m)
