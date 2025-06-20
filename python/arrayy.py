## Running Sum of Array Elements
class solution:
    def run(self,arr):
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]+arr[i]
        return arr
s=solution()
arr=list(map(int,input().split()))
print(s.run(arr))

## If input is given inside code

#s = solution()
#print(s.run([1, 2, 3, 4, 5]))
