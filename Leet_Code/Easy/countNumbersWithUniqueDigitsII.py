# Leet Code Algo 3032. Count Numbers With Unique Digits II

def checkUniqueNum(num: int) -> bool:
        numStr = str(num)
        hashNums = {}
        for char in numStr:
            if char not in hashNums:
                hashNums[char] = 1
            else:
                return False
        return True

def numberCount(a: int, b: int) -> int:
    counter = 0
    for i in range(a, b+1):
        temp = checkUniqueNum(i)
        if temp:
            counter += 1
    return counter

print(numberCount(1,20))
print(numberCount(9,19))
print(numberCount(80,120))