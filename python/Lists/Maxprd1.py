#eeeerrrrrrrrrrrrrroorrrrrr
a=[-2,6,-3,-10,0,2]
b=0
for i in range(0,len(a),3):
    c=a[i]*a[i+1]*a[i+2]
    if c>b:
        b=c
        print(i,i+1,i+2)
print(b)

