# Leet Code Algo 3880. Minimum Absolute Difference Between Two Values

def minAbsoluteDifference(nums):
    len_nums = len(nums)
    one_counter = 0
    two_counter = 0
    one_array = []
    two_array = []
    for i in range(len_nums):
        if nums[i] == 1:
            one_counter += 1
            one_array.append(i)
        elif nums[i] == 2:
            two_counter += 1
            two_array.append(i)
    if one_counter == 0 or two_counter == 0:
        return - 1
    min_diff = 100
    for j in range(len(one_array)):
        for k in range(len(two_array)):
            if abs(one_array[j]-two_array[k]) < min_diff:
                min_diff = abs(one_array[j]-two_array[k])
    return min_diff

print(minAbsoluteDifference([1,0,0,2,0,1]))
print(minAbsoluteDifference([1,0,1,0]))