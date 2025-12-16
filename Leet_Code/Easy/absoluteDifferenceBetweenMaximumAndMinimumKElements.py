# Leet Code Algo 3774. Absolute Difference Between Maximum and Minimum Difference K Elements

def absDifference(nums, k):
    if len(nums) == 1:
        return 0
    sorted_nums = sorted(nums)
    len_sorted_nums = len(sorted_nums)
    min_sum = 0
    for i in range(k):
        min_sum += sorted_nums[i]
    max_sum = 0
    for j in range(k):
        max_sum += sorted_nums[len_sorted_nums - 1 - j]
    return max_sum - min_sum

print(absDifference([5,2,2,4], 2))
print(absDifference([100], 1))