# Leet Code Algo 2903. Find Indices With and Value Difference I

def findIndicesWithIndexAndValueDifferenceI(nums, indexDifference, valueDifference):
    if len(nums) == 1 and indexDifference == 0 and valueDifference == 0:
        return [0, 0]
    answer = []
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if (abs(nums[i] - nums[j]) >= valueDifference and
                abs(i - j) >= indexDifference):
                    answer.append(i)
                    answer.append(j)
                    return answer
    answer.append(-1)
    answer.append(-1)
    return answer
                
print(findIndicesWithIndexAndValueDifferenceI([5,1,4,1], 2, 4))
print(findIndicesWithIndexAndValueDifferenceI([0,1], 0, 0))
print(findIndicesWithIndexAndValueDifferenceI([1,2,3], 2, 4))
print(findIndicesWithIndexAndValueDifferenceI([0], 0, 0))
print(findIndicesWithIndexAndValueDifferenceI([3], 0, 0))