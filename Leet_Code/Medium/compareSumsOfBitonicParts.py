# Leet Code Algo 3909. Compare Sums of Bitonic Parts.

def compareBitonicSums(nums):
    max_val = 0
    max_idx = 0
    for i in range(len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i
    sum_asc = sum(nums[:max_idx+1])
    sum_desc = sum(nums[max_idx:]) 
    if sum_asc > sum_desc:
        return 0
    elif sum_asc < sum_desc:
        return 1
    else:
        return -1

print(compareBitonicSums([1,3,2,1]))
print(compareBitonicSums([2,4,5,2]))
print(compareBitonicSums([1,2,4,3]))