# Leet Code Algo 3741. Minimum Distance Between Three Equal Elements II

def minimumDistance(nums):
    hash_nums = {}
    for i in range(len(nums)):
        if nums[i] not in hash_nums:
            hash_nums[nums[i]] = [i]
        else:
            hash_nums[nums[i]].append(i)
    min_val = 1000000
    for key, value in hash_nums.items():
        if len(value) > 2:
            for j in range(1, len(value)-1):
                if abs(value[j-1] - value[j]) + abs(value[j] - value[j+1]) + abs(value[j-1] - value[j+1]) < min_val:
                    min_val = abs(value[j-1] - value[j]) + abs(value[j] - value[j+1]) + abs(value[j-1] - value[j+1])
    return -1 if min_val == 1000000 else min_val

print(minimumDistance([1,2,1,1,3]))
print(minimumDistance([1,1,2,3,2,1,2]))
print(minimumDistance([1]))