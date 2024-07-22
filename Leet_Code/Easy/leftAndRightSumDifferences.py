# Leet Code Algo 2574. Left and Right Sum Differences.

def leftAndRightSumDifferences(nums):
    rightSum = 0
    leftSum = 0
    leftArray = [0]
    rightArray = [0] * len(nums)
    answer = [0] * len(nums)
    for i in range(len(nums) - 1):
        leftSum += nums[i]
        leftArray.append(leftSum)
        rightSum += nums[len(nums) - 1 - i]
        rightArray[len(nums) - 2 - i] = rightSum
    for j in range(len(leftArray)):
        answer[j] = abs(leftArray[j] - rightArray[j])
    return answer

print(leftAndRightSumDifferences([10,4,8,3]))
print(leftAndRightSumDifferences([1]))
        