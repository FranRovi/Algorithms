# Hacker Rank Algo. Minimum Absolute Difference in an Array

def minimumAbsoluteDifference(arr):
    # Write your code here
    minDifference = 999999
    sortedArr = sorted(arr)
    for i in range(len(sortedArr) -1):
        if abs(sortedArr[i] - sortedArr[i + 1]) < minDifference:
            minDifference = abs(sortedArr[i] - sortedArr[i + 1])
    return minDifference

print(minimumAbsoluteDifference([3,-7,0]))
print(minimumAbsoluteDifference([-59,-36,-13,1,-53,-92,-2,-96,-54,75]))
print(minimumAbsoluteDifference([1,3,71,68,17]))