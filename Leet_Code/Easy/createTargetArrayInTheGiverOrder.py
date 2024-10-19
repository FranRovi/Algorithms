# Leet Code Algo 1389. Create Target Array in the Given Order

def createTargetArrayInTheGiverOrder(nums, index):
    answer = []
    for i in range(len(nums)):
        answer.insert(index[i], nums[i])
    return answer

print(createTargetArrayInTheGiverOrder([0,1,2,3,4], [0,1,2,2,1]))
print(createTargetArrayInTheGiverOrder([1,2,3,4,0], [0,1,2,3,0]))