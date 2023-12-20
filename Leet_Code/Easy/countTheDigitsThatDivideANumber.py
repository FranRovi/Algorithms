# Leet Code Algo 2520. Count the Digits That Divide a Number

def countTheDigitsThatDivideANumber(num):
    numStr = str(num)
    counter = 0
    for i in range(len(numStr)):
        if num % int(numStr[i]) == 0:
            counter += 1
    return counter

print(countTheDigitsThatDivideANumber(7))
print(countTheDigitsThatDivideANumber(121))
print(countTheDigitsThatDivideANumber(1248)) 