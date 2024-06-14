# Leet Code Algo 2169. Count Operations To Obtain Zero

def countOperations(num1, num2):
    if num1 == num2:
        if num1 > 0:
            return 1
        else:
            return 0
    counter = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        counter += 1
    return counter

print(countOperations(2, 3))
print(countOperations(10, 10))