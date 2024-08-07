# Leet Code Algo 2160. Minimum Sum of Four Digit Number After Splitting Digits


def minimumSum(num):
    numList = list(map(str, str(num)))
    for i in range(len(numList)-1):
        for j in range(i+1, len(numList)):
            if int(numList[i]) > int(numList[j]):
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
    return int(numList[0] + numList[3]) + int(numList[1] + numList[2])
    
print(minimumSum(2932))
print(minimumSum(4009))

                


