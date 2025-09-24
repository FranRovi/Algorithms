# Leet Code Algo 1338. Reduce Array Size to The Half

def minSetSize(arr):
    len_arr = len(arr)
    half_len = len(arr) // 2
    hash_nums = {}
    for n in arr:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
    if len_arr == len(hash_nums):
        return len_arr // 2
    sorted_hash = dict(sorted(hash_nums.items(), key=lambda item:item[1], reverse=True))
    total_sum = 0
    counter = 0
    for k, v in sorted_hash.items():
        total_sum += v
        counter += 1
        if total_sum >= half_len:
            return counter

print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(minSetSize([7,7,7,7,7,7]))
print(minSetSize([1,9]))