#Increasing triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()