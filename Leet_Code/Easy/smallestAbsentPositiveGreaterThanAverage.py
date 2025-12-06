# Leet Code Algo 3678. Smallest Absent Positive Greater Than Average.

def smallestAbsent(nums):
    total_sum = 0 
    hash_nums = {}
    for n in nums:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
        total_sum += n
    avg_arr = int(total_sum / len(nums))

    if avg_arr < 0:
        avg_arr = 0
    idx = avg_arr + 1 
    while True:
        if idx not in hash_nums:
            return idx
        idx += 1

print(smallestAbsent([3,5]))
print(smallestAbsent([-1,1,2]))
print(smallestAbsent([4,-1]))
print(smallestAbsent([-34]))