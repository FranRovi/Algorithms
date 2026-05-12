# Leet Code Algo 3925. Concatenate Array With Reverse.

def concatWithReverse(nums):
    len_nums = len(nums)
    for i in range(len_nums-1,-1,-1):
        nums.append(nums[i])
    return nums

print(concatWithReverse([1,2,3]))
print(concatWithReverse([1]))