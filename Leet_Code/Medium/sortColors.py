# Leet Code Algo 72. Sort Colors

def sortColors(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums) - 1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1,]))