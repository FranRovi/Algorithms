# Leet Code Algo 2229. Check if an Array is Consecutive

def isConsecutive(nums):
    min_val = 10001
    if len(nums) == 1 and nums[0] == 0:
        return True
    hash_nums = {}
    for num in nums:
        if num < min_val:
            min_val = num
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    
    for i in range(min_val, len(nums) + min_val):
        if i not in hash_nums:
            return False
    return True

print(isConsecutive([1,3,4,2]))
print(isConsecutive([1,3]))
print(isConsecutive([3,5,4]))
print(isConsecutive([0]))
print(isConsecutive([0,1,2,3,4]))