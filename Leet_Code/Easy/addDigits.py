# Leet Code 258. Add Digits

def addDigits(num):
    strNum = str(num)
    if len(strNum) == 1:
        return int(strNum)
    numVal = 0
    while len(strNum) > 1:
        numVal = 0
        for i in range(len(strNum)):
            numVal += int(strNum[i])
        strNum = str(numVal)
    return numVal
    
    
print(addDigits(38))
print(addDigits(978))
print(addDigits(0))
    
