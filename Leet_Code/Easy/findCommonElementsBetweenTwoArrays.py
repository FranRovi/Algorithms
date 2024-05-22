# Leet Code Algo 2956. Find Common Elements Between Two Arrays

def findIntersectionValues(nums1, nums2):
    counterNum1 = 0
    counterNum2 = 0
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            counterNum1 += 1
    for j in range(len(nums2)):
        if nums2[j] in nums1:
            counterNum2 += 1
    return [counterNum1, counterNum2]

print(findIntersectionValues([4,3,2,3,1],[2,2,5,2,3,6]))
print(findIntersectionValues([3,4,2,3],[1,5]))