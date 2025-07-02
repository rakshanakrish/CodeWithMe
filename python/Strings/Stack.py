a="{[()]}"
b={'{':'}','[':']','(':')'}
c=[]
for i in a:
    if i in "([{":
        c.append(i)
    elif i in b.values():
        if not c or b[c[-1]] != i:
            print(False)
            break
        c.pop()
else:
    print(len(c)==0)
