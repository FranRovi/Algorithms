# Leet Code Algo 3550. Smallest Index With Digit Sum Equal to Index

def smallestIndex(nums):
    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] < 10 and nums[i] == i:
                return i
        else:
            temp_str_num = str(nums[i])
            total_sum = 0
            for j in range(len(temp_str_num)):
                total_sum += int(temp_str_num[j])
            if total_sum == i:
                return i
    return -1

print(smallestIndex([1,3,2]))
print(smallestIndex([1,10,11]))
print(smallestIndex([1,2,3]))