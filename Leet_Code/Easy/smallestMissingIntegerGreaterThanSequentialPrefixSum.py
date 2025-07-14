# Leet Code Algo 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum.

def missingInteger(nums):
    prefix_arr = [nums[0]]
    largest_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] + 1 == nums[i]:
            prefix_arr.append(nums[i])
        else:
            break
    for num in nums:
        if num > largest_num:
            largest_num = num
    prefix_arr_sum = sum(prefix_arr)
    answer = prefix_arr_sum 
    
    while True:
        if answer not in nums:
            break
        else:
            answer += 1
    return answer

print(missingInteger([1,2,3,2,5]))
print(missingInteger([3,4,5,1,12,14,13]))
print(missingInteger([29,30,31,32,33,34,35,36,37]))
print(missingInteger([4,5,6,7,8,8,9,4,3,2,7]))
print(missingInteger([1,2,3,9,2,10,8,3,10,2]))