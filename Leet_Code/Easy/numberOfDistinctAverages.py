# Leet Code Algo 2465. Number of Distinct Averages

def distinctAverages(nums):
    sortedNums = sorted(nums)
    avgSmLg = set()
    for i in range(int(len(sortedNums)/2)):
        avgSmLg.add((sortedNums[i] + sortedNums[len(sortedNums) - 1 - i]) / 2)
    return len(avgSmLg)

print(distinctAverages([4,1,4,0,3,5]))
print(distinctAverages([1,100]))
print(distinctAverages([9,5,7,8,7,9,8,2,0,7]))