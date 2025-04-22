def myfunct(n):
    return abs(n-50)


thislist = [100,34,56,50,22]
thislist.sort(key=myfunct)
print(thislist)
