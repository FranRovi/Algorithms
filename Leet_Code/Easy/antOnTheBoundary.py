# Leet Code Algo 3028. Ant on the Boundary

def antOnTheBoundary(nums):
    counter = 0
    currentPos = 0
    for i in range(len(nums)):
        currentPos += nums[i]
        if currentPos == 0:
            counter += 1
    return counter

print(antOnTheBoundary([2,3,-5]))
print(antOnTheBoundary([3,2,-3,-4]))
