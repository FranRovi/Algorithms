# Leet Code Algo 3512. Minimum Operations to Make Array Sum Divisible by K.

def minOperations(nums, k):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum % k

print(minOperations([3,9,7],5))
print(minOperations([4,1,3],4))
print(minOperations([3,2],6))


