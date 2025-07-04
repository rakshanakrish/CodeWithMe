nums=[1,3,5,6]
target=7
l,h=0,len(nums)-1
while l<=h:
    m=(l+h)//2
    if nums[m]>target :
        h-=1 
    elif l==h:
        print(l)   
    if nums[m]<target:
        l+=1
    


