n="12345"
l=len(n)
for i in range(l):
    for j in range(l):
        if i==j or i+j==4:
            print(n[i],end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(l):
    for j in range(l):
        if i==j or i+j==4:
            print(n[j],end=" ")
        else:
            print(" ",end=" ")
    print()
