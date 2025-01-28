# Leet Code Algo 349. Intersection of Two Arrays

def intersection(nums1, nums2):
    num_set1 = set(nums1)
    num_set2 = set(nums2)
    intersection = num_set1 & num_set2
    return list(intersection)

print(intersection([1,2,2,1],[2,2]))
print(intersection([4,9,5],[9,4,9,8,4]))

