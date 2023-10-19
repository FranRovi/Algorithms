# Leet Code 268. Missing Number

def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    return i

print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
