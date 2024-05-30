# Leet Code Algo 2367. Number of Arithmetic Triplets

def arithmeticsTriplets(nums, diff):
    counter = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums) -1):
            for k in range(j+1, len(nums)):
               if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                   counter += 1
    return counter 

print(arithmeticsTriplets([0,1,4,6,7,10], 3))
print(arithmeticsTriplets([4,5,6,7,8,9], 2))
