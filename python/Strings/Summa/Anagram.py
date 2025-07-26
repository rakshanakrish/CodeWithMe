a=input()
b=input()
c=list(a)
d=list(b)
if all(char in c for char in b):
    print(True)
else:
    print(False)

""" listen
    silent """
# not close code
"""Better to use
    sorted(a)==sorted(b)
            or
    from collections import Counter
    Counter(a) == Counter(b)"""