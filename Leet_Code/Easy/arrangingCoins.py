# Leet Code Algo 441. Arranging Coins

def arrangingCoins(n):
    level = 0
    
    while n > level:
        level += 1
        n -= level
    
    return level

print(arrangingCoins(5))
print(arrangingCoins(8))
print(arrangingCoins(1))