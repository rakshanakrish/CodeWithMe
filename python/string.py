a=['r','a','k','s','h','a','n','a']
mini=0
maxi=0
for i in range(len(a)):
    if a[i]>a[maxi]:
        maxi=i
    if a[i]<a[mini]:
        mini=i

a[mini],a[maxi]=a[maxi],a[mini]
print(a)