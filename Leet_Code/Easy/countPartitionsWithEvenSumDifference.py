# Leet Code Algo 3432. Count Partitions with Even Sum Difference

def countPartitions(nums):
    counter = 0
    left_arr = [nums[0]]
    right_arr = nums[1:]
    if (sum(left_arr) - sum(right_arr)) % 2 == 0:
        counter += 1
    for i in range(1, len(nums) - 1):
        left_arr.append(nums[i])
        del right_arr[0]
        if (sum(left_arr) - sum(right_arr)) % 2 == 0:
            counter += 1
    return counter

print(countPartitions([10,10,3,7,6]))
print(countPartitions([1,2,2]))
print(countPartitions([2,4,6,8]))
    