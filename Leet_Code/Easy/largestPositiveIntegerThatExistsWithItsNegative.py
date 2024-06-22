# Leet Code Algo 2441. Largest Positive Integer That Exists With Its Negative

def findMaxK(nums):
    hashNums = {}
    for i in range(len(nums)):
        if nums[i] not in hashNums:
            hashNums[nums[i]] = 1
        else:
            hashNums[nums[i]] += 1
    sortedNumsHash = sorted(hashNums.items(), reverse = True)
    sortedNumsHashDict = dict(sortedNumsHash)
    for key, value in sortedNumsHashDict.items():
        if (key *-1) in sortedNumsHashDict:
            return key
    return -1

print(findMaxK([-1,2,-3,3]))
print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))