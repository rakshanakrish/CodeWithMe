nums = [1, 1, 2, 2, 3]
a={}
for i,n in enumerate(nums):
    a[n] = i
print(list(a.keys()))