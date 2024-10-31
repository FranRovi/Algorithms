# Leet Code Algo 1827. Minimum Operations To Make Array Increasing

def minOperations(nums):
    counter = 0
    if len(nums) == 1:
        return 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            temp = abs(nums[i] - nums[i-1])
            counter += temp + 1
            nums[i] += temp + 1
    return counter

print(minOperations([1,1,1]))
print(minOperations([1,5,2,4,1]))
print(minOperations([8])) 