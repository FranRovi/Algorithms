# Leet Code Algo 2869. Minimum Time To Collect all Elements

def minOperations(nums, k):
    target_arr = []
    for i in range(1,k+1):
        target_arr.append(i)
    counter = 0
    for j in range(len(nums)-1, -1,-1):
        if len(target_arr) == 0:
            break
        else:
            counter += 1
            if nums[j] in target_arr:
                target_arr.remove(nums[j])
    return counter

print(minOperations([3,1,5,4,2], 2))
print(minOperations([3,1,5,4,2], 5))
print(minOperations([3,2,5,3,1], 3))