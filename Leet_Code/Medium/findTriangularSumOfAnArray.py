# Leet Code Algo 2221. Find Triangular Sum of an Array

def findTriangularSumOfAnArray(nums):
    if len(nums) == 1:
        return nums[0]
    newNums = nums
    while len(newNums) > 1:
        for i in range(len(newNums) - 1):
            if newNums[i] + newNums[i+1] > 9:
                tempStr = str(newNums[i] + newNums[i+1])
                newNums[i] = int(tempStr[-1])
            else:
                newNums[i] = newNums[i] + newNums[i+1]
        newNums.pop()
    return newNums[0]
        
print(findTriangularSumOfAnArray([1,2,3,4,5]))
print(findTriangularSumOfAnArray([5]))
        
