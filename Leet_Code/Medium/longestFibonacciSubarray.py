# Leet Code Algo 3708. Longest Fibonacci Subarray

def longestSubarray(nums):
    max_counter = 0
    current_counter = 2
    for i in range(2, len(nums)):
        if nums[i-2] + nums[i-1] == nums[i]:
            current_counter += 1
        else:
            if current_counter > max_counter:
                max_counter = current_counter
            current_counter = 2
    if current_counter > max_counter:
        return current_counter
    return max_counter

print(longestSubarray([1,1,1,1,2,3,5,1]))
print(longestSubarray([5,2,7,9,16]))
print(longestSubarray([1000000000,1000000000,1000000000]))