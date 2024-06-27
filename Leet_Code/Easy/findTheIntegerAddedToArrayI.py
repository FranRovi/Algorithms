# Leet Code Algo 3131. Find the Integer Added to Array I

def addedInteger(nums1, nums2):
    nums1Sorted = sorted(nums1)
    nums2Sorted = sorted(nums2)
    return nums2Sorted[0] - nums1Sorted[0]

print(addedInteger([2,6,4],[9,7,5]))
print(addedInteger([10], [5]))