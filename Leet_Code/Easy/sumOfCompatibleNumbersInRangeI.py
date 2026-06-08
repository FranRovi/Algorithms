# Leet Code Algo 3954. Sum of Compatible Numbers in Range I

def sumOfGoodIntegers(n, k):
    start = max(1, n-k)
    total_sum = 0
    for i in range(start, n+k+1):
        if abs(n-i) <= k and n & i == 0:
            total_sum += i
    return total_sum

print(sumOfGoodIntegers(2,3))
print(sumOfGoodIntegers(5,1))
print(sumOfGoodIntegers(1,13))