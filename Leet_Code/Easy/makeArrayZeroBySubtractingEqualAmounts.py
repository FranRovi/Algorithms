# Leet Code Algo 2357. Make Array Zero by Subtracting Equal Amounts

def minimumOperations(nums):
    if len(nums) == 1:
        if nums[0] == 0:
            return 0
        else:
            return 1
    
    set_nums = set(nums)
    if 0 in set_nums:
        set_nums.remove(0)

    return len(set_nums)

print(minimumOperations([1,5,0,3,5]))
print(minimumOperations([0]))
print(minimumOperations([10]))