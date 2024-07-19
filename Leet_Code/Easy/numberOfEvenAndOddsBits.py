# Leet Code Algo 2595 Number of Even and Odds Bits

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
    return bit

def evenOddBit(n):
    answer = [0,0]
    binaryNum = intToBinary(n)
    for i in range(len(binaryNum)):
        if binaryNum[i] == 1:
            if i % 2 == 0:
                answer[0] += 1
            else:
                answer[1] += 1
    return answer
        
    
print(evenOddBit(50))
print(evenOddBit(2))
print(evenOddBit(5))


    