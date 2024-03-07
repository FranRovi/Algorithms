# Leet Code Algo 2206. Divide Array Into Equal Pairs

def divideArrayIntoEqualPairs(nums):
    if len(nums) % 2 != 0:
        return False
    hashNums = {}
    for i in range(len(nums)):
        if nums[i] not in hashNums:
            hashNums[nums[i]] = 1
        else:
             hashNums[nums[i]] += 1
    print(hashNums)
    for key, value in hashNums.items():
        if value % 2 != 0:
            return False
    return True
    
    
print(divideArrayIntoEqualPairs([1,2,3,4]))
print(divideArrayIntoEqualPairs([3,2,3,2,2,2]))