# Leet Code Algo 3264. Final Array State AFter K Multiplication Operations I

def getFinalState(nums, k, multiplier):
    for i in range(k):
        minVal = nums[0]
        minIdx = 0
        for j in range(len(nums)):
            if minVal > nums[j]:
                minVal = nums[j]
                minIdx = j
        nums[minIdx] = minVal * multiplier
    return nums

print(getFinalState([2,1,3,5,6], 5, 2))
print(getFinalState([1,2], 3, 4))  
    