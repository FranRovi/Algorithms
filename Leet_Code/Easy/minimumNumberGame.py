# Leet Code Algo 2974. Minimum Number Game

def findTwoMinVals(nums):
    minVal = 101
    idxMinVal = 0
    secondMinVal = 101
    idxSecondMinVal = 0
    for i in range(len(nums)):
        if nums[i] < minVal:
            idxSecondMinVal = idxMinVal
            secondMinVal = minVal
            idxMinVal = i
            minVal = nums[i]
        else:
            if nums[i] >= minVal and nums[i] <= secondMinVal:
                idxSecondMinVal = i
                secondMinVal = nums[i]
    if idxMinVal < idxSecondMinVal:
        del nums[idxMinVal]
        del nums[idxSecondMinVal - 1]
    else:
        del nums[idxSecondMinVal] 
        del nums[idxMinVal -1]
    return [minVal, secondMinVal]
                
def minimumNumberGame(nums):
    answer = []
    if len(nums) == 2:
        return[nums[0], nums[1]] if nums[0] > nums[1] else [nums[1], nums[0]] 
    for i in range(int(len(nums) / 2)):
        valuesToAdd = findTwoMinVals(nums)
        answer.append(valuesToAdd[1])
        answer.append(valuesToAdd[0])
    return answer

print(minimumNumberGame([5,4,3,2]))
print(minimumNumberGame([2,5]))
print(minimumNumberGame([2,7,9,6,4,6]))

