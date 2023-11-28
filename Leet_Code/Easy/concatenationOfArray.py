# Leet Code Algo 1929. Concatenation Of Array

def concatenationOfArray(nums):
    answer = [0] * (2 * len(nums))
    for i in range(len(nums)):
        answer[i] = nums[i]
        answer[len(nums) + i] = nums[i]
    return answer

print(concatenationOfArray([1,2,1]))
print(concatenationOfArray([1,3,2,1]))