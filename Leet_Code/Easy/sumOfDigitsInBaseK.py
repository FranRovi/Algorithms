# Leet Code Algo 1837. Sum Of Digits in Base K

def sumBase(n, k):
    strAnswer = ""
    while n >= k:
        strAnswer += str(n % k)
        n = n // k
    if n > 0:
        strAnswer += str(n)
    totalSum = 0 
    for char in strAnswer:
        totalSum += int(char)
    return totalSum

print(sumBase(34,6))
print(sumBase(10,10))
print(sumBase(42,2))