# Leet Code Algo 338. Counting Bits

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

def countBits(n):
    answer = []
    for i in range(n + 1):
        temp = intToBit(i)
        counter = 0
        for j in range(len(temp)):
            if temp[j] == 1:
                counter += 1
        answer.append(counter)
    return answer

print(countBits(2))
print(countBits(5)) 