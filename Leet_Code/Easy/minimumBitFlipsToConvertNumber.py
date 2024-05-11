# Leet Code Algo 2220. Minimum Bit Flips To Convert Number

def convertIntToBinary(n):
    reverseAnswer = []
    answer = []
    while n > 1:
        if n % 2 == 0:
            reverseAnswer.append(0)
        else: 
            reverseAnswer.append(1)
        n = n // 2
    reverseAnswer.append(1) if n == 1 else reverseAnswer.append(0)    
    for i in range(len(reverseAnswer) -1, -1, -1):
        answer.append(reverseAnswer[i])
    return answer

def minBitFlips(start, goal):
    startBinary = convertIntToBinary(start)
    goalBinary = convertIntToBinary(goal)
    counter = 0
    
    if len(startBinary) != len(goalBinary):
        difLenStart = abs(len(startBinary) - len(goalBinary))
        if len(startBinary) > len(goalBinary):
            for i in range(difLenStart):
                goalBinary.insert(0, 0)
        else:
            for j in range(difLenStart):
                startBinary.insert(0, 0)    
    for k in range(len(startBinary)):
        if startBinary[k] != goalBinary[k]:
            counter += 1
    return counter


print(minBitFlips(10, 7))
print(minBitFlips(3, 4))
