# Leet Code 283. Move Zeroes

def moveZeroes(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            temp = nums[i]
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                else: 
                    j += 1
    return nums

print(moveZeroes([0,1,0,2,0]))
print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,1,0,91,16]))
print(moveZeroes([0]))