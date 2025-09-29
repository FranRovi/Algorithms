# Leet Code Algo 3452. Sum of Good Numbers

def sumOfGoodNumbers(nums, k):
    total_sum = 0
    len_nums = len(nums)
    for i in range(len_nums):
        if i + k >= len_nums:
            if nums[i] > nums[i-k]:
                total_sum += nums[i]
        elif i - k < 0:
            if nums[i] > nums[i+k]:
                total_sum += nums[i]
        elif nums[i] > nums[(i+k) % len_nums] and nums[i] > nums[(i-k) % len_nums]:
            total_sum += nums[i]
    return total_sum

print(sumOfGoodNumbers([1,3,2,1,5,4], 2))
print(sumOfGoodNumbers([2,1],1))
print(sumOfGoodNumbers([16,25,36],1))
print(sumOfGoodNumbers([37,13,29],1))