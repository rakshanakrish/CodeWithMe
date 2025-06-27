arr = "madam"
ispal=True
left, right = 0, len(arr) - 1
while left < right:
    if arr[left]!=arr[right]:
        ispal=False
        break
    left+=1
    right-=1
print(ispal)