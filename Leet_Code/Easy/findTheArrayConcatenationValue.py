# Leet Code Algo 2562. Find the Array Concatenation Value

def findTheArrayConcVal(nums):
    totalSum = 0
    rightIdx = len(nums) - 1
    for i in range(int(len(nums)/2)):
        tempStrNum = str(nums[i]) + str(nums[rightIdx])
        # print(tempStrNum)
        totalSum += int(tempStrNum)
        rightIdx -= 1
    if len(nums) % 2 == 0:
        return totalSum
    else:
        #print(int(len(nums)/2) + 1)
        return totalSum + nums[int(len(nums)/2)]


print(findTheArrayConcVal([7,52,2,4]))
print(findTheArrayConcVal([5,14,13,8,12]))