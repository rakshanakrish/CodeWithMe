n=6
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print("  ",end="") #double spacing
    for j in range(i+1):
        print("*",end=" ")
    print()