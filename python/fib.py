n=int(input())
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-2)+F(n-1)
print(F(n))
