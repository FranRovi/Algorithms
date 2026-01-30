# Leet Code Algo 976. Largest Perimeter Triangle

def largestPerimeter(nums):
    len_nums = len(nums)
    sorted_nums = sorted(nums, reverse = True)
    for i in range(2, len_nums):
        if sorted_nums[i] + sorted_nums[i-1] > sorted_nums[i-2]:
            return sorted_nums[i] + sorted_nums[i-1] + sorted_nums[i-2]
    return 0

print(largestPerimeter([2,1,2]))
print(largestPerimeter([1,2,1,10]))