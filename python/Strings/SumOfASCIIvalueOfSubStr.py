a = "ab"
n = len(a)
total_sum = 0

for i in range(n):
    for j in range(i, n):
        for ch in a[i:j+1]:
            total_sum += ord(ch)

print(total_sum)




