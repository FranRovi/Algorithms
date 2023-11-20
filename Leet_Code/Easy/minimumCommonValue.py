# Leet Code Algo 2540. Minimum Common Value


def minimumCommonValue(nums1, nums2):
    i = j = index = 0
    if (nums1[-1] < nums2[0] or
        nums1[0] > nums2[-1]):
        return -1
    arrLen = len(nums1) + len(nums2)
    while index < arrLen:
        # if (i >= len(nums1) and
        #     j >= len(nums2)):
        #         break
        if nums1[i] == nums2[j]:
            return nums1[i]
        else:
            if nums1[i] > nums2[j] and j < len(nums2) - 1:
                    j += 1
            else:
                if i < len(nums1) - 1:
                    i += 1
        index += 1     
    return -1
    
            
# print(minimumCommonValue([1,2,3], [2,4]))
# print(minimumCommonValue([1,2,3,6], [2,3,4,5]))
# print(minimumCommonValue([5,15,16,20,22,39,43,44,44,55,61,62,62,64,72,73,81,88,90,95], [2,8,9,11,12,13,26,29,38,49,50,51,58,63,67,72,75,82,92,96]))
# print(minimumCommonValue([3,5], [2]))
# print(minimumCommonValue([34,225,328,530,823,834,902,989], [24,30,115,121,160,173,239,265,335,362,449,557,597,624,697,766,775,881,898,919]))
# print(minimumCommonValue([5,15,16,20,22,39,43,44,44,55,61,62,62,64,72,73,81,88,90,95], [2,8,9,11,12,13,26,29,38,49,50,51,58,63,67,72,75,82,92,96]))
print(minimumCommonValue([2], [1, 2]))
