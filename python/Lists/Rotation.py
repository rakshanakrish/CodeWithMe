#Left Rotation
a=[1,2,3,4,5]
n=len(a)
k=2
k=k%n
print(a[k:]+a[:k])

"""for right rotation we use
print(a[-k:]+a[:-k])"""