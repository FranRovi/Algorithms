# Leet Code Algo 1874. Minimize Product Sum of Two Arrays

def minProductSum(nums1, nums2):
    sortedNumsOne = sorted(nums1, reverse = True)
    sortedNumsTwo = sorted(nums2)
    totalSum = 0
    for i in range(len(sortedNumsOne)):
        totalSum += sortedNumsOne[i] * sortedNumsTwo[i]
    return totalSum

print(minProductSum([5,3,4,2],[4,2,2,5]))
print(minProductSum([2,1,4,5,7],[3,2,4,8,6]))