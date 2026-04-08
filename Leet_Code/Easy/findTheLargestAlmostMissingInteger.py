# Leet Code Algo 3471. Find the Largest Almost Missing Integer

def largestInteger(nums, k):
    hash_nums = {}
    temp = nums[:k]
    for i in range(k):
        if temp[i] not in hash_nums:
            hash_nums[temp[i]] = 1
    for j in range(k, len(nums)):
        temp = temp[1:]
        temp.append(nums[j])
        for l in range(k):
            if temp[l] not in hash_nums:
                hash_nums[temp[l]] = 1
            else:
                hash_nums[temp[l]] += 1
    max_val = -1
    for key, value in hash_nums.items():
        if value == 1:
            if key > max_val:
                max_val = key
    return max_val

print(largestInteger([3,9,2,1,7], 3))
print(largestInteger([3,9,7,2,1,7], 4))
print(largestInteger([0,0], 1))
print(largestInteger([0,0], 2))