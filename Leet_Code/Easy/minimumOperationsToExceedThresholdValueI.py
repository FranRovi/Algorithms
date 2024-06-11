# Leet Code Algo 3065. Minimum Operations to Exceed Threshold Value I

def minOperations(nums, k):
    counter = 0
    for i in range(len(nums)):
        if nums[i] < k:
            counter += 1
    return counter

print(minOperations([2,11,10,1,3],10))
print(minOperations([1,1,2,4,9],1))
print(minOperations([1,1,2,4,9], 9))