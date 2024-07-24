# Leet Code Algo 868. Binary Gap

def intToBit(n):
    reversedBit = []
    bitNumStr = ""
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    for i in range(len(reversedBit)-1,-1,-1):
        bitNumStr += str(reversedBit[i])
    return bitNumStr

def binaryGap(n):
    if n == 0:
        return 0
    
    maxDif = 0
    firstIdx = 0
    secondIdx = 0
    
    bit = intToBit(n)
    for j in range(1, len(bit)):
        if bit[j] == '1':
            secondIdx = j
            if secondIdx - firstIdx > maxDif:
                maxDif = secondIdx - firstIdx
            firstIdx = secondIdx
    return maxDif
        
        


print(binaryGap(22))
print(binaryGap(8))
print(binaryGap(5))