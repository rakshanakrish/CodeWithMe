a,b=map(str,input().split())
for i in range(len(a)):
    c=a[-i:]+a[:-i]
    if c==b:
        print("true")
        exit()
else:
    print("false")