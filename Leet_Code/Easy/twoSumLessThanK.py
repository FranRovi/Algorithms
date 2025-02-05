# Leet Code Algo 1099. Two Sum Less Than K

def twoSumLessThanK(nums, k):
    max_sum = -1
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < k:
                if nums[i] + nums[j] > max_sum: 
                    max_sum = nums[i] + nums[j]
    return max_sum

print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))
print(twoSumLessThanK([10,20,30], 15))