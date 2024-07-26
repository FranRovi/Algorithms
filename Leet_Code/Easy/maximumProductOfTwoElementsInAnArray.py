# Leet Code Algo 1464. Maximum Product of Two Elements in an Array

def maxProduct(nums):
    if len(nums) == 2:
        return (nums[0] - 1) * (nums[1] -1)
    if nums[0] > nums[1]:
        largest = nums[0]
        largestIdx = 0
        secondLargest = nums[1]
        secondLargestIdx = 1
    else:
        largest = nums[1]
        largestIdx = 1
        secondLargest = nums[0]
        secondLargestIdx = 0
    for i in range(2, len(nums)):
        if nums[i] > largest:
            secondLargest = largest
            secondLargestIdx = largestIdx
            largest = nums[i]
            largestIdx = i
        else:
            if nums[i] > secondLargest:
                secondLargest = nums[i]
                secondLargestIdx = i
    return (nums[largestIdx] - 1) * (nums[secondLargestIdx] -1)   

print(maxProduct([3,4,5,2]))
print(maxProduct([1,5,4,5]))
print(maxProduct([3,7]))
