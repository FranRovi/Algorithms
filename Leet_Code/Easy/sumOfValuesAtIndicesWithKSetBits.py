# Leet Code Algo 2859. Sum of Values at Indices With K Set Bits

def intToBit(n):
    reverseBinary = []
    answer = ""
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
    for i in range(len(reverseBinary)- 1, -1,-1):
        answer += str(reverseBinary[i])
    return answer
    
def sumIndicesWithKSetBits(nums, k):
    totalSum = 0
    for i in range(len(nums)):
        counter = 0
        tempBinary = intToBit(i)
        # print(tempBinary)
        for j in range(len(tempBinary)):
            if tempBinary[j] == '1':
                counter += 1
        if counter == k:
            totalSum += nums[i]
    return totalSum
            
    
print(sumIndicesWithKSetBits([5,10,1,5,2], 1))
print(sumIndicesWithKSetBits([4,3,2,1], 2))