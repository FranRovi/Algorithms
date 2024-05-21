# Leet Code Algo 3099. Harshad Number

def harshadNumber(x):
    sumOfNums = 0
    strNum = str(x)
    for i in range(len(strNum)):
        sumOfNums += int(strNum[i])
    if x % sumOfNums == 0:
        return sumOfNums
    return -1

print(harshadNumber(18))
print(harshadNumber(23))
print(harshadNumber(264))