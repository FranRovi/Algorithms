# Leet Code 215. Kth Element in an Array

def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]

print(findKthLargest([3,2,1,5,4,6], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
