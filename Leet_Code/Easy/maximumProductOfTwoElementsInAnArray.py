# Leet Code Algo 1464. Maximum Product of Two Elements in an Array

def maxProduct(nums):
    maxTotal = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i]-1) * (nums[j]-1) > maxTotal:
                maxTotal = (nums[i]-1) * (nums[j]-1)
    print(maxTotal)

maxProduct([3,4,5,2])
maxProduct([1,5,4,5])
maxProduct([3,7])
