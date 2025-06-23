a=[1,1,2,1,3,5,1]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
maxf=0
maxe=None
for key in freq:
    if freq[key] > maxf:
        maxf=freq[key]
        maxe=key
print(maxe)
