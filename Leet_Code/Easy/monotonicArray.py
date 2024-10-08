# Leet Code Algo 896. Monotonic Array

def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            isDecreasing = False
        if nums[i] > nums[i-1]:
            isIncreasing = False
        if isIncreasing == False and isDecreasing == False:
            return False
    return True

print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))