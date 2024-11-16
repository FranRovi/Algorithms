# Leet Code Algo 2908. Minimum Sum of Mountain Triplets I

def minimumSum(nums):
    minSum = 9999
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j +1, len(nums)):
                if nums[i] < nums[j] and nums[k] < nums[j]:
                    if nums[i] + nums[j] + nums[k] < minSum:
                        minSum = nums[i] + nums[j] + nums[k]
    if minSum != 9999:
        return minSum
    return -1

print(minimumSum([8,6,1,5,3]))
print(minimumSum([5,4,8,7,10,2]))
print(minimumSum([6,5,4,3,4,5])) 