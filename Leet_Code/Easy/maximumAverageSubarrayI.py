# Leet Code Algo 643. Maximum Average Subarray I

def findMaxAverage(nums, k):
    max_sum = total_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        total_sum = total_sum + nums[i] - nums[i-k]
        if total_sum > max_sum:
            max_sum = total_sum
    return max_sum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))
print(findMaxAverage([7,4,5,8,8,3,9,8,7,6], 7))
print(findMaxAverage([8,0,1,7,8,6,5,5,6,7], 5))
