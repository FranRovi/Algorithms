# Leet Code Algo 3682. Minimum Index Sum of Common Elements

def minimumSum(nums1, nums2):
    hash_nums = {}
    for i in range(len(nums1)):
        if nums1[i] not in hash_nums:
            hash_nums[nums1[i]] = [i]
    for j in range(len(nums2)):
        if nums2[j] in hash_nums:
            if len(hash_nums[nums2[j]]) == 1:
                hash_nums[nums2[j]].append(j)
    min_val = 100000
    is_no_match = True
    for key, value in hash_nums.items():
        if len(value) == 2:
            is_no_match = False
            if sum(value) < min_val:
                min_val = sum(value)
    if is_no_match:
        return -1
    return min_val

print(minimumSum([3,2,1],[1,3,1]))
print(minimumSum([5,1,2],[2,1,3]))
print(minimumSum([6,4],[7,8]))

           