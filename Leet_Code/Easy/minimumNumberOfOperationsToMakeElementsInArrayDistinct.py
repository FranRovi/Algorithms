# Leet Code Algo 3396. Minimum Number of Operations to Make Elements in Array Distinct.

def minimumOperations(nums):
    hash_nums = {}
    len_nums_original = len(nums)
    for num in nums:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    nums_of_ele = len(nums)
    start_idx = 0
    end_idx = 3
    counter = 0
    while True:
        if len(hash_nums) > len(nums) - start_idx:
            return counter
        elif len(hash_nums) != len(nums) - start_idx:
            elements_to_remove = nums[start_idx:end_idx]
            for j in range(len(elements_to_remove)):
                if elements_to_remove[j] in hash_nums:
                    if  hash_nums[elements_to_remove[j]] > 1:
                        hash_nums[elements_to_remove[j]] -= 1
                    else:
                        del hash_nums[elements_to_remove[j]]
            start_idx = end_idx
            end_idx += 3
            counter += 1
        else:
            return counter

print(minimumOperations([1,2,3,4,2,3,3,5,7]))
print(minimumOperations([4,5,6,4,4]))
print(minimumOperations([6,7,8,9]))
    

