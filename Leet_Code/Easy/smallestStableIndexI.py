# Leet Code Algo 3903. Smallest Stable Index I

def firstSmallestIndex(nums, k):
    max_val = nums[0]
    min_val = 1000000000
    for n in nums:
        if n < min_val:
            min_val = n
    if max_val - min_val <= k:
        return 0
    left_arr = [nums[0]]
    right_arr = nums
    len_nums = len(nums)
    for i in range(1, len_nums):
        left_arr.append(nums[i])
        if (max(left_arr) - min(right_arr[i:])) <= k:
            return i 
    return -1

print(firstSmallestIndex([5,0,1,4], 3))
print(firstSmallestIndex([3,2,1], 1))
print(firstSmallestIndex([0], 0))
print(firstSmallestIndex([8,6,3,6,3,7], 4))
print(firstSmallestIndex([22942,22942,22942,22942,22942,22942,22942,22942,22942,22942], 6))
