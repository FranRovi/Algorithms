# Leet Code Algo 3701. Compute Alternating Sum

def alternatingSum(nums):
    total_sum = 0
    for k in range(len(nums)):
        if k % 2 == 0:
            total_sum += nums[k]
        else:
            total_sum -= nums[k]
    return total_sum

print(alternatingSum([1,3,5,7]))
print(alternatingSum([100]))