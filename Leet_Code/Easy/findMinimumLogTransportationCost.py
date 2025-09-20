# Leet Code Algo 3560. Find Minimum Log Transportation Cost

def minCuttingCost(n,m,k):
    largest = n if n > m else m
    dif = largest - k
    if largest > k:
        return (largest - dif) * dif
    else:
        return 0  
print(minCuttingCost(6,5,5))
print(minCuttingCost(4,4,6))