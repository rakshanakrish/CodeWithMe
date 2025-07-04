a="{[()]}"
b={'{':'}','[':']','(':')'}
c=[]
for i in a:
    if i in "([{":
        c.append(i)
    elif i in b.values():
        if not c or b[c.pop()]!=i:
            print(False)
            exit()
print(not c)