# Leet Code 1281. Subtract the Product and Sum of Digits of an Integer

def subtractTheProductAndSumOfDigitsOfAnInteger(n):
    totalProduct = 1
    totalSum = 0
    strNum = str(n)
    
    for i in range(len(strNum)):
        totalProduct *= int(strNum[i])
        totalSum += int(strNum[i])
    
    return totalProduct - totalSum

print(subtractTheProductAndSumOfDigitsOfAnInteger(234))
print(subtractTheProductAndSumOfDigitsOfAnInteger(4421))