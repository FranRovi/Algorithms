# Leet Code Algo 2161. Partition Array According To Given Pivot

def pivotArray(nums, pivot):
    less_arr = []
    equal_arr = []
    greater_arr = []
    for i in range(len(nums)):
        if nums[i] < pivot:
            less_arr.append(nums[i])
        elif nums[i] > pivot:
            greater_arr.append(nums[i])
        else:
            equal_arr.append(nums[i])
    return less_arr + equal_arr + greater_arr

print(pivotArray([9,12,5,10,14,3,10], 10))
print(pivotArray([-3,4,3,2], 2))