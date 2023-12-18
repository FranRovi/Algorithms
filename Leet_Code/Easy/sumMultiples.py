# Leet Code Algo 2652. Sum Multiples

def sumMultiples(n):
    divNums = []
    for i in range(1, n + 1):
        if (i % 3 == 0 or i % 5 == 0
        or  i % 7 == 0):
            divNums.append(i)
    return sum(divNums)

print(sumMultiples(7))
print(sumMultiples(10))
print(sumMultiples(9))