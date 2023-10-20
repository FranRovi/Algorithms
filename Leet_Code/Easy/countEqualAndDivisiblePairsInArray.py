# Leet Code 2176. Count Equal an Divisible Pairs in an Array

def countEqualAndDivisiblePairsInAnArray(nums, k):
    counter = 0
    for i in range(len(nums) - 1):
        for j in range(1, (len(nums))):
            if (nums[i] == nums[j]
                and i < j
                and j < len(nums) 
                and ((i * j) % k == 0)):
                    counter += 1
    return counter
            
print(countEqualAndDivisiblePairsInAnArray([3,1,2,2,2,1,3], 2))
print(countEqualAndDivisiblePairsInAnArray([1,2,3,4], 1))