class solution:
    def run (self,arr):
        arr=[1,2,3,4,5]
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]+arr[i]
        return i