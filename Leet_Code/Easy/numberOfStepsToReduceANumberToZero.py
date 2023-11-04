# Leet Code 1342 Number of Steps to Reduce a Number To Zero

def numberOfStepsToReduceANumberToZero(num):
    numOfSteps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        numOfSteps += 1
        # print(num)
    return numOfSteps

print(numberOfStepsToReduceANumberToZero(14))
print(numberOfStepsToReduceANumberToZero(8))
print(numberOfStepsToReduceANumberToZero(123))