from collections import deque 
a=[3,4,8,1,6,7,9]
a.sort()
pen=deque()
for i in range(len(a)):
    if i%2==0:
        pen.append(a[i])
    else:
        pen.appendleft(a[i])
p=list(pen)
print(*p)

    
