# Leet Code Algo 3151. Special Array I

def isArraySpecial(nums):
    for i in range(1, len(nums)):
        if (nums[i] % 2 == 0 and nums[i-1] % 2 != 0 or
        nums[i] % 2 != 0 and nums[i-1] % 2 == 0):
            continue
        else:
            return False
    return True

print(isArraySpecial([1]))
print(isArraySpecial([2,1,4]))
print(isArraySpecial([4,3,1,6])) 