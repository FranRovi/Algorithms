# Leet Code Algo 485. Max Consecutive Ones

def maxConsecutiveOnes(nums):
    maxOnes = 0
    temp = 0
    idx = 0
    while idx < len(nums):
        if nums[idx] == 0:
            if temp > maxOnes:
                maxOnes = temp
            temp = 0
        else:
            temp += 1
        idx += 1
    if temp > maxOnes:
        maxOnes = temp    
    return maxOnes

print(maxConsecutiveOnes([1,1,0,1,1,1]))
print(maxConsecutiveOnes([1,0,1,1,0,1]))
        