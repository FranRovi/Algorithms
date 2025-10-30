# Leet Code Algo 3226. Number of Bit Changes to Make Two Integers Equal

def intToBit(n):
        reversedBit = []
        bitNumArr = []
        while n >= 2:
            if n % 2 == 0:
                reversedBit.append(0)
            else:
                reversedBit.append(1)
            n = n // 2
        reversedBit.append(1)
        for i in range(len(reversedBit)-1,-1,-1):
            bitNumArr.append(reversedBit[i])
        return bitNumArr

def minChanges(n: int, k: int) -> int:
    num1 = intToBit(n)
    num2 = intToBit(k)

    len_num1 = len(num1)
    len_num2 = len(num2)

    dif_len = abs(len_num1 - len_num2)
    for j in range(dif_len):
        if len_num1 > len_num2:
            num2.insert(0,0)
        else:
            num1.insert(0,0)
    counter = 0
    for k in range(len(num1)):
        if num1[k] == 1 and num2[k] == 0:
            counter += 1
        elif num1[k] == 0 and num2[k] == 1:
            return -1 
    return counter

print(minChanges(13, 4))
print(minChanges(21, 21))
print(minChanges(14, 13))