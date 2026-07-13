# Leet Code Algo 724. Find Pivot Index

def pivotIndex(nums):
    len_nums = len(nums)
    left_sum = [0]* len_nums
    for i in range(1, len_nums):
        left_sum[i] = nums[i-1] + left_sum[i-1]
    right_sum = [0]* len_nums
    for j in range(len_nums-1, 0, -1):
        right_sum[j-1] = nums[j] + right_sum[j]
    for k in range(len_nums):
        if right_sum[k] == left_sum[k]:
            return k
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))