a=[1,2,3,4,5,6]
l=r=0
while r<len(a):
    w=sum(a[l:r+1])
    if w>10:
        l+=1
    else:
        print(a[l:r+1],w)
        r+=1
    
    

