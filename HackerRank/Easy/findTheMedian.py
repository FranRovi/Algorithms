# Hacker Rank Algo Find The Median

def findTheMedian(arr):
    sortedArr = sorted(arr)
    return sortedArr[int(len(sortedArr) / 2)]

print(findTheMedian([5,3,1,2,4]))