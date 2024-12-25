# Leet Code Algo 1403. Minimum Subsequence in Non-Increasing Order

def minSubsequence(nums):
    sortedNums = sorted(nums)
    leftIdx = 0
    rightIdx = len(nums) - 1
    leftSum = 0
    rightSum = 0
    answer = []
    idx = 0
    while idx < len(nums):
        if rightSum <= leftSum:
            answer.append(sortedNums[rightIdx])
            rightSum += sortedNums[rightIdx]
            rightIdx -= 1
        else:
            leftSum += sortedNums[leftIdx]
            leftIdx += 1
        idx += 1
    if leftSum >= rightSum:
        answer.append(sortedNums[leftIdx - 1])
    return answer

print(minSubsequence([4,3,10,9,8]))
print(minSubsequence([4,4,7,6,7]))
print(minSubsequence([4,10,2,6,1]))