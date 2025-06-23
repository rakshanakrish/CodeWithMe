def wave(arr):
    for i in range(0, len(arr)-1, 2):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80]
a=wave(arr)
print(a)

        
