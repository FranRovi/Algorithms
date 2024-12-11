# Leet Code Algo 2600. K Items With Maximum Sum

def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    totalSum = 0
    arrNums = []
    for i in range(numOnes):
        arrNums.append(1)
    for j in range(numZeros):
        arrNums.append(0)
    for l in range(numNegOnes):
        arrNums.append(-1)
    for n in range(k):
        totalSum += arrNums[n]
    return totalSum

print(kItemsWithMaximumSum(3,2,0,2))
print(kItemsWithMaximumSum(3,2,0,4))
