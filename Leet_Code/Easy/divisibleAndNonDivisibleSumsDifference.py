# Leet Code Algo 2894. Divisible and Non-divisible Sums Difference 

def divisibleAndNonDivsibleSumsDifference(n, m):
    div = []
    nonDiv = []
    for i in range(1, n + 1):
        if i % m == 0:
            div.append(i)
        else:
            nonDiv.append(i)
    return sum(nonDiv) - sum(div)
    
print(divisibleAndNonDivsibleSumsDifference(10, 3))
print(divisibleAndNonDivsibleSumsDifference(5, 6))
print(divisibleAndNonDivsibleSumsDifference(5, 1))
