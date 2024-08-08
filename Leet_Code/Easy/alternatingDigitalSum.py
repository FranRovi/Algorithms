# Leet Code Algo 2544. Alternating Digit Sum

def alternateDigitSum(n):
    totalSum = 0
    strNum = str(n)
    for i in range(len(strNum)):
        if i % 2 == 0:
            totalSum += int(strNum[i])
        else:
            totalSum -= int(strNum[i])
    return totalSum

print(alternateDigitSum(521))
print(alternateDigitSum(111))
print(alternateDigitSum(886996))