# Leet Code Algo 476. Number Compliment

def intToBinary(n):
    reversedBit = []
    bit = []
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    for i in range(len(reversedBit)-1, -1, -1):
        bit.append(reversedBit[i])
    # print(bit)
    return bit

def binaryToInt(s):
    totalSum = 0
    lenS = len(s)
    for i in range(len(s)):
        totalSum += 2 ** i * int(s[lenS - 1 - i])
    return totalSum  

def findComplement(num):
    binaryNum = intToBinary(num)
    binaryComplement = ""
    for i in range(len(binaryNum)):
        if binaryNum[i] == 0:
            binaryComplement += "1"
        else:
            binaryComplement += "0"
    # print(binaryComplement)
    answer = binaryToInt(binaryComplement)
    return answer 

print(findComplement(5))
print(findComplement(1))