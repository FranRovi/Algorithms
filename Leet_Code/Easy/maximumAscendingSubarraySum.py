# Leet Code Algo 1800. Maximum Ascending Subarray Sum

def maxAscendingSum(nums):
    maxSum = nums[0]
    temp = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            temp += nums[i]
        else:
            if temp > maxSum:
                maxSum = temp
            temp = nums[i]
    if temp > maxSum:
        maxSum = temp
    return maxSum

print(maxAscendingSum([10,20,30,5,10,50]))
print(maxAscendingSum([10,20,30,40,50]))
print(maxAscendingSum([12,17,15,13,10,11,12])) 