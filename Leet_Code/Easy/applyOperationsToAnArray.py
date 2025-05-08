# Leet Code Algo 2460. Apply Operations to an Array

def applyOperations(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
    answer = [0] * len(nums)
    idx = 0
    for num in nums:
        if num != 0:
            answer[idx] = num
            idx += 1
    return answer

print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([0,1]))
