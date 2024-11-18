# Leet Code Algo 3345. Smallest Divisible Digit Product I

def smallestNumber(n, t):
    strN = str(n)
    digit_prod = 1
    for char in strN:
        digit_prod *= int(char)
    if digit_prod % t == 0:
        return n
    else:
        return smallestNumber(n+1, t)
    
print(smallestNumber(10, 2))
print(smallestNumber(15, 3))