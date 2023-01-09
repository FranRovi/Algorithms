# Exercise 136

# Given a non-empty array of integers nums, every element appears twice except
# one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Ouput: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Ouput: 4

# Example 3:
# Input: nums = [1]
# Ouput: 1

def singleNumber(nums):
    arrDict = {}
    for num in nums:
        if (num in arrDict.keys()):
             del arrDict[num]
        else:
             arrDict[num] = 1
    for element in arrDict.keys():
        return(element)

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))
