# Leet Code Algo 3046. Split the Array

def isPossibleToSplit(nums):
    hashNums = {}
    for i in range(len(nums)):
        if nums[i] not in hashNums:
            hashNums[nums[i]] = 1
        else:
            hashNums[nums[i]] += 1
    
    for key, value in hashNums.items():
        if value > 2:
            return False
    return True

print(isPossibleToSplit([1,1,2,2,3,4]))
print(isPossibleToSplit([1,1,1,1]))