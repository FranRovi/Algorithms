# Leet Code Algo 2873. Maximum Value of an Ordered Triplet I

def maximumTripletValue(nums):
    maxVal = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j +1, len(nums)):
                    if (nums[i] - nums[j]) * nums[k] > maxVal:
                        maxVal = (nums[i] - nums[j]) * nums[k]
    if maxVal != 0:
        return maxVal
    return 0

print(maximumTripletValue([12,6,1,2,7]))
print(maximumTripletValue([1,10,3,4,19]))
print(maximumTripletValue([1,2,3]))