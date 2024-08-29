# Leet Code Algo 2475. Number Of Unequal Triplets in Array

def unequalTriplets(nums):
    counter = 0
    for i in range(len(nums) - 2):
            for j in range(len(nums) - 1):
                for k in range(len(nums)):
                    if ((i < j and j < k and i < k) and
                    (nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k])):
                        counter += 1        
    return counter

print(unequalTriplets([4,4,2,4,3]))
print(unequalTriplets([1,1,1,1,1]))
        