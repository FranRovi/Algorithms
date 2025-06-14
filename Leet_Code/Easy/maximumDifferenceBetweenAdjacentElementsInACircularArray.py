# Leet Code Algo 3423. Maximum Difference Between Adjacent Elements In a Circular Array

def maxAdjacentDistance(nums):
    max_diff = -1
    for i in range(1, len(nums)):
        if abs(nums[i-1] - nums[i]) > max_diff:
            max_diff = abs(nums[i-1] - nums[i])
    if abs(nums[0] - nums[-1]) > max_diff:
            max_diff = abs(nums[0] - nums[-1])
    return max_diff

print(maxAdjacentDistance([1,2,4]))
print(maxAdjacentDistance([-5,-10,-5]))