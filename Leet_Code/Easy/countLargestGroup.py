# Leet Code Algo 1399. Count Largest Group

def countLargestGroup(n):
    counter = 0
    largestGroup = 0
    hashGroups = {}
    for i in range(1, n + 1):
        if i < 10:
            hashGroups[i] = [i]
        else:
            tempNum = str(i)
            tempSum = 0
            for j in range(len(tempNum)):
                tempSum += int(tempNum[j])
            if tempSum not in hashGroups:
                hashGroups[tempSum] = [(int(tempNum))]
            else:
                hashGroups[tempSum].append(int(tempNum))
    for key, value in hashGroups.items():
        if len(value) > largestGroup:
            counter = 1
            largestGroup = len(value)
        elif largestGroup == len(value):
            counter += 1
    return counter 

print(countLargestGroup(13))
print(countLargestGroup(2))
print(countLargestGroup(24))
