arr=[1,3,4,5,6]
target = 10
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Indices: {i},{j}")
            print(f"Values: {arr[i]}, {arr[j]}")
            break
    else:
        continue
    break





