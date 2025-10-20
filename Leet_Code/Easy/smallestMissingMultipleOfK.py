# Leet Code Algo 3718. Smallest Missing Multiple of K

def missingMultiple(nums, k):
    hash_nums = {}
    for n in nums:
        hash_nums[n] = 1
    idx = 1
    while True:
        if k * idx not in hash_nums:
            return k * idx
        else:
            idx += 1

print(missingMultiple([8,2,3,4,6], 2))
print(missingMultiple([1,4,7,10,15], 5))