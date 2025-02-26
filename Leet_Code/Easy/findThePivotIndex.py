# Leet Code 2485. Find the Pivot Index

def findThePivotIndex(n):
    if n == 1:
        return 1
    nums = [i for i in range(1, n + 1)]
    left_sum = sum(nums[:nums[len(nums) -1]])
    right_sum = nums[len(nums) - 1]
    idx = len(nums) - 1
    while left_sum >= right_sum:
        left_sum -= nums[idx]
        right_sum += nums[idx-1]
        if left_sum == right_sum:
            return nums[idx-1]
        idx -= 1  
    return -1

    ### Ineffcient Approach because it recreates the array at every iteration an recounts the sum of its elements ###
    # if n == 1:
    #     return 1
    # nums = [i for i in range(1, n + 1)]
    # left_arr = nums[:nums[len(nums) -1]]
    # right_arr = [nums[len(nums) - 1]]
    # while len(left_arr) > len(right_arr) and sum(left_arr) > sum(right_arr):
    #     left_arr.pop()
    #     right_arr.append(left_arr[-1])

    #     if sum(left_arr) == sum(right_arr):
    #         return left_arr[-1]  
    # return -1
    
print(findThePivotIndex(8))
print(findThePivotIndex(1))
print(findThePivotIndex(4))    