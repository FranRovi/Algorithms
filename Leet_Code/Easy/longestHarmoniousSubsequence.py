# Leet Code Algo 594. Longest Harmonious Subsequence

def findLHS(nums):
    hash_nums = {}
    for n in nums:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
    hash_nums_sorted = dict(sorted(hash_nums.items()))
    arr_keys = list(hash_nums_sorted.keys())
    max_length = 0
    for i in range(len(arr_keys) -1):
        if arr_keys[i+1] - arr_keys[i] == 1:
            if hash_nums_sorted[arr_keys[i]] + hash_nums_sorted[arr_keys[i+1]] > max_length:
                max_length = hash_nums_sorted[arr_keys[i]] + hash_nums_sorted[arr_keys[i+1]]
    return max_length

print(findLHS([1,3,2,2,5,2,3,7]))
print(findLHS([1,2,3,4]))
print(findLHS([1,1,1,1]))
print(findLHS([1,3,5,7,9,11,13,15,17]))