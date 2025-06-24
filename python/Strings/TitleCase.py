a="this is a string"
b=a.split()
c=' '.join(i.capitalize() for i in b)
print(c)
print(a.title())