# Leet Code Algo 1317. Convert Integer to the sum of Two No-Zero Integers

def getNoZeroIntegers(n):
    first_num = n - 1
    second_num = 1

    while "0" in str(first_num) or "0" in str(second_num):
        first_num -= 1
        second_num += 1
    
    return [first_num,second_num]

print(getNoZeroIntegers(2))
print(getNoZeroIntegers(11))
print(getNoZeroIntegers(1010))