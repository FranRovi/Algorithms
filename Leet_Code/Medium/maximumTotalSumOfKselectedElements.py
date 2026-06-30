# Leet Code Algo 3974. Maximum Total Sum of K Selected Elements

def maxSum(nums, k, mul):
    sorted_nums = sorted(nums, reverse= True)
    total_sum = 0
    for i in range(k):
        if mul > 1:
            total_sum += sorted_nums[i] * mul
        else:
            total_sum += sorted_nums[i]
        mul -= 1
    return total_sum

print(maxSum([6,1,2,9], 3, 2))
print(maxSum([3,7,5,2], 2, 4))
print(maxSum([4,4], 1, 1))