# Leet Code Algo 2824. Count Pairs Whose Sum is Less Than Target

def countPairsWhoseSumIsLessThanTarget(nums, target):
    counter = 0
    for i in range(len(nums) -1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                counter +=1
    return counter

print(countPairsWhoseSumIsLessThanTarget([-1,1,2,3,1], 2))
print(countPairsWhoseSumIsLessThanTarget([-6,2,5,-2,-7,-1,3], -2))