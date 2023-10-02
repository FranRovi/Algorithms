def containsDuplicate(nums):
    dictNums = {}
    for i in range(len(nums)):
        if (dictNums.get(nums[i]) == None):
            dictNums[nums[i]] = 1
        else:
            return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))