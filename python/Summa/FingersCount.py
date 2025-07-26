def countf(n):
    r=n%8
    if r==0:
        return 2
    elif r<5:
        return r
    else:
        return 10-r
n=int(input())
print(countf(n))