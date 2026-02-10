# Leet Code Algo 3379. Transformed Array

def constructTransformedArray(nums):
    len_nums = len(nums)
    answer = [0] * len_nums
    for i in range(len_nums):
        temp = nums[i]
        answer[i] = nums[(i + temp) % len_nums]
    return answer

print(constructTransformedArray([3,-2,1,1]))
print(constructTransformedArray([-1,4,-1]))