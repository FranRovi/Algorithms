# Leet Code 3712. Sum of Elements With Frequency Divisible by K.

def sumDivisibleByK(nums, k):
    hash_nums = {}
    for n in nums:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
    total_sum = 0
    for key, value in hash_nums.items():
        if value % k == 0:
            total_sum += key * value
    return total_sum

print(sumDivisibleByK([1,2,2,3,3,3,3,4], 2))
print(sumDivisibleByK([1,2,3,4,5], 2))
print(sumDivisibleByK([4,4,4,1,2,3], 3))