# Leet Code Algo 2932. Maximum Strong Pair XOR I

def maximumStrongPairXOR(nums):
    max_val = 0
    len_nums = len(nums)
    for i in range(len_nums-1):
        for k in range(i+1, len_nums):
            if abs(nums[i]-nums[k]) <= min(nums[i],nums[k]):
                if nums[i] ^ nums[k] > max_val:
                    max_val = nums[i] ^ nums[k]
    return max_val
    
print(maximumStrongPairXOR([1,2,3,4,5]))
print(maximumStrongPairXOR([10,100]))
print(maximumStrongPairXOR([5,6,25,30]))