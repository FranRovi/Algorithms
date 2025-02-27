# Leet Code 461. Hamming Distance

def intToBinary(n):
    reversedBit = []
    bit = []
    if n == 0:
        return [0]
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    for i in range(len(reversedBit)-1, -1, -1):
        bit.append(reversedBit[i])
    return bit

def hammingDistance(x, y):
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        return 1
    counter = 0
    binaryX = intToBinary(x)
    binaryY = intToBinary(y)    
    if len(binaryX) > len(binaryY):
        difArrX = len(binaryX) - len(binaryY)  
        for i in range(difArrX):
            binaryY.insert(0,0)
    if len(binaryX) < len(binaryY):
        difArrY =  len(binaryY) - len(binaryX)  
        for j in range(difArrY):
            binaryX.insert(0,0)
    for k in range(len(binaryX)):
        if binaryX[k] != binaryY[k]:
            counter += 1
    return counter

print(hammingDistance(1, 4))
print(hammingDistance(3, 1))
print(hammingDistance(0, 1))
print(hammingDistance(0, 10))
    