# Leet Code Algo 3427. Sum of Variable Length Subarrays

def subarraySum(nums):
    total_sum = nums[0]
    for i in range(1, len(nums)):
        start = max(0, i - nums[i])
        total_sum += sum(nums[start:i+1])
    return total_sum

print(subarraySum([2,3,1]))
print(subarraySum([3,1,1,2]))