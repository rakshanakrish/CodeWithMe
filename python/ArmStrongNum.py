"""def a(num):
    digits=[int(d)for d in digits(str(num))]
    n=len(str(num))
    a=sum(d**n for d in digits )"""
n=153
a=list(str(n))
b=len(a)
c=0
for i in a:
    c+=int(i)**b
if c==n:
    print(True)
else:
    print(False)