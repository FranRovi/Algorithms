# Leet Code Algo 3833. Count Dominant Indeces

def dominantIndeces(nums):
    if len(nums) < 3:
        if len(nums) == 2:
            return 1 if nums[0] > nums[1] else 0
        else:
            return 0
    curr_val = float(nums[0])
    total_sum = sum(nums[1:])
    num_ele = len(nums) - 1
    counter = 0
    if curr_val > (total_sum / num_ele):
        counter += 1
    for i in range(1,num_ele):
        curr_val = float(nums[i])
        num_ele -= 1
        total_sum -= int(curr_val)
        if curr_val > (total_sum / num_ele):
            counter += 1
    return counter

print(dominantIndeces([5,4,3]))
print(dominantIndeces([4,1,2]))
print(dominantIndeces([58,89]))
print(dominantIndeces([45,70,38]))
print(dominantIndeces([12]))