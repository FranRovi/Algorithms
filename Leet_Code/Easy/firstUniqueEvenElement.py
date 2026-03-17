# Leet Code Algo 3866. First Unique Even Element

def firstUniqueEven(nums):
    hash_even_nums = {}
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            if nums[i] not in hash_even_nums:
                hash_even_nums[nums[i]] = [i]
            else:
                hash_even_nums[nums[i]].append(i)
    min_val = 100
    for key, value in hash_even_nums.items():
        if len(value) == 1:
            return key
    if min_val == 100:
        return -1
    
print(firstUniqueEven([3,4,2,5,4,6]))
print(firstUniqueEven([4,4]))
print(firstUniqueEven([2,10]))
print(firstUniqueEven([8,2,]))
            
    