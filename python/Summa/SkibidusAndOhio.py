num=int(input())
for i in range(num):
    n,m=(int(input()) , 1)
    a= list(map(int, input().split()))
    b=int(input())
    f=0
    for i in range(len(a) -1):
        if a[i] <= a[i+1]:
            f=1 
    if f==1:
        a[i+1] = b - a[i+1]
        a.sort(reverse=True)
        print(a)
    

