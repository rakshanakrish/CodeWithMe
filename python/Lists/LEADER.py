n=int(input())
a=list(map(int,input().split()))  # Read the array
b=[]                              # To store leaders
r=float('-inf')                   # Store max so far from the right

for i in reversed(a):             # Traverse from right to left
    if i > r:
        b.append(i)               # If current element is greater than max so far, it’s a leader
        r = i                     # Update max

print(*b[::-1])                   # Print leaders in correct order (reverse again)
