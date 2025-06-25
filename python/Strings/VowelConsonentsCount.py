n=input()
a=''.join(n.split()) #n.replace(" ","")
aa="aeiou"
v=0
c=0
for i in a:
    if i in aa:
        v+=1
    else:
        c+=1
print(a)
print(v)
print(c)

