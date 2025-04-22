prices = [7, 1, 5, 3, 6, 4]
max_n=0
n=0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[i]<prices[j]:
            n = prices[j] - prices[i]
            max_n = max(max_n, n)

print("profit:",max_n)
           
        
            
