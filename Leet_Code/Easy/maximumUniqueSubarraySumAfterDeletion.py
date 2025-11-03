# Leet Code Algo 3487. Maximum Unique Subarray Sum After Deletion.

def maxSum(nums):
    set_positive_nums = set()
    set_negative_nums = set()

    for n in nums:
        if n > 0:
            set_positive_nums.add(n)
        else:
            set_negative_nums.add(n)

    set_negative_nums = list(set_negative_nums)
    sorted_negative_nums = sorted(set_negative_nums)

    if len(sorted_negative_nums) >= 1:
        sorted_negative_nums = sorted_negative_nums[-1]
    if sum(set_positive_nums) > 0:
        return sum(set_positive_nums)
    else:
        return sorted_negative_nums
    
print(maxSum([1,2,3,4,5]))
print(maxSum([1,1,0,1,1]))
print(maxSum([1,2,-1,-2,1,0,-1]))
print(maxSum([-100]))
print(maxSum([1,-5]))
