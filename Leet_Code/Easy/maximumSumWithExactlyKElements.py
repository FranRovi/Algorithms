# Leet Code Algo 2656. Maximum Sum With Exactly K Elements

def maximumSize(nums, k):
    maxNum = 0
    maxIdx = 0
    total = 0
    for i in range(len(nums)):
        if nums[i] > maxNum:
            maxNum = nums[i]
            maxIdx = i
    for j in range(k):
        total += maxNum
        maxNum += 1
        nums[maxIdx] = maxNum
    return total

print(maximumSize([1,2,3,4,5], 3))
print(maximumSize([5,5,5], 2))
    