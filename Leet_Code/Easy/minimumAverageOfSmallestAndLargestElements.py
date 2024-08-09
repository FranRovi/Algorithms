# Leet Code Algo 3194. Minimum Average of Smallest and Largest Elements

def minimumAverage(nums):
    averageArr = []
    while len(nums) > 0:
        minElement = nums[0]
        maxElement = nums[0]
        for i in range(len(nums)):
            if nums[i] < minElement:
                minElement = nums[i]
            if nums[i] > maxElement:
                maxElement = nums[i]
        averageArr.append((minElement+maxElement) / 2)
        nums.remove(minElement)
        nums.remove(maxElement)
    smallestVal = averageArr[0]
    for j in range(1, len(averageArr)):
        if smallestVal > averageArr[j]:
            smallestVal = averageArr[j]
    return smallestVal
            

print(minimumAverage([7,8,3,4,15,13,4,1]))
print(minimumAverage([1,9,8,3,10,5]))
print(minimumAverage([1,2,3,7,8,9]))
        