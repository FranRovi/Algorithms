# Leet Code Algo 3370. Smallest Number With All Set Bits

def intToBit(n):
    reverseBinary = []
    if n == 0:
        reverseBinary = [0]
    elif n == 1:
        reverseBinary = [1]
    else:
        while n >= 2:
            if n % 2 == 0:
                reverseBinary.append(0)
            else:
                reverseBinary.append(1)
            n = n // 2
        reverseBinary.append(1)
    return reverseBinary

def smallestNumber(n):
    binary_num = intToBit(n)
    smallest_num = 0
    for i in range(len(binary_num) -1, -1, -1):
        smallest_num += 2 ** i
    return smallest_num

print(smallestNumber(5))
print(smallestNumber(10))
print(smallestNumber(3))