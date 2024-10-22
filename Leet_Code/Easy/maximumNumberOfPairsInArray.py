# Leet Code Algo 2341. Maximum Numbers of Pairs in Array

def numberOfPairs(nums):
    counterOfPairs = 0
    remainingElem = 0
    hashNums = {}
    for num in nums:
        if num not in hashNums:
            hashNums[num] = 1
        else:
            del hashNums[num]
            counterOfPairs += 1
    for key, value in hashNums.items():
        remainingElem += 1
    return [counterOfPairs, remainingElem]

print(numberOfPairs([1,3,2,1,3,2,2]))
print(numberOfPairs([1,1]))
print(numberOfPairs([0]))