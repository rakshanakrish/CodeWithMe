a = [2, 11, 7, 9]
t = 9

def g(a):
    h = {}
    for i, v in enumerate(a):
        if t - v in h:
            return h[t - v], i   
        else:
            h[v] = i

x, y= g(a)
print(x, y)


