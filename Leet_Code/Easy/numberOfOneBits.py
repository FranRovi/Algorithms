# Leet Code Algo 191. Number 1 of Bits

def intToBit(n):
    reversedBit = []
    counter = 0
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    for i in range(len(reversedBit)):
        if reversedBit[i] == 1:
            counter += 1
    return counter

print(intToBit(11))
print(intToBit(128))
    