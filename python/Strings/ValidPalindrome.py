s="A man, a plan, a canal: Panama"
a=""
#import re
for i in s:
    if i.isalnum():
        a+=i.lower()
#a = re.sub(r'[^A-Za-z0-9]', '', s).lower()
print(a==a[::-1])
    