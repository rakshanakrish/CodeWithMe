nums = [-1, 0, 1, 2, -1, -4]
w=0
for i in range(1,len(nums)):
    if nums[i] + nums[i-1] +nums[w] ==0:
        print(nums[i] ,nums[i-1] ,nums[w])
        w+=1
    continue



