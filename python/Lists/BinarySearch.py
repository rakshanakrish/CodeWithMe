a = [20, 52, 61, 89, 100]
n = 89
l = 0
u = len(a) - 1

while l <= u:
    m = (l + u) // 2
    if a[m] == n:
        print(m)
        break
    elif a[m] < n:
        l = m + 1
    else:
        u = m - 1


