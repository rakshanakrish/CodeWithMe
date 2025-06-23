a=[1,2,3,-4,-1,4]
p=[]
n=[]
for i in a:
    if i<0:
        n.append(i)
    else:
        p.append(i)
i=0
j=0
result=[]
while i<len(p)and j<len(n):
    result.append(p[i])
    result.append(n[j])
    i+=1
    j+=1
while i<len(p):
    result.append(p[i])
    i+=1
while j<len(n):
    result.append(n[j])
    j+=1
print(result)


    
