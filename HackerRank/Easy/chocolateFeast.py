# Hacker Rank Algo. Chocolate Feast

def chocolateFeast(n, c, m):
    total = 0
    candies = n // c
    total += candies
    while candies >= m:
        temp = candies // m
        total += temp
        candies = candies % m
        candies += temp
    return total

print(chocolateFeast(15, 3, 2))
print(chocolateFeast(10, 2, 5)) 
print(chocolateFeast(12, 4, 4)) 
print(chocolateFeast(6, 2, 2))  