# Leet Code Algo 3392. Count Subarray of Length Three With a Condition.

def countSubarrays(nums):
    counter = 0
    for i in range(1, len(nums)-1):
        if nums[i-1] + nums[i+1] == nums[i]/2:
            counter += 1
    return counter

print(countSubarrays([1,2,1,4,1]))
print(countSubarrays([1,1,1]))
print(countSubarrays([-1,-4,-1,4]))

