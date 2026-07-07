# Add Leet Code Algo 3912. Valid Elements in an Array.

def findMax(nums):
    max_num = 0
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
    return max_num
    
def findValidElements(nums):
    if len(nums) <= 2:
        return nums
    left_max = nums[0]
    right_max = findMax(nums[2:])
    answer = [nums[0]]
    ptr = nums[1]
    for i in range(2, len(nums)-1):
        if ptr > left_max:
            answer.append(ptr)
        elif ptr > right_max:
            answer.append(ptr)
        if ptr > left_max:
            left_max = ptr
        right_max = findMax(nums[i+1:])
        ptr = nums[i]
    if ptr > left_max or ptr > right_max:
        answer.append(ptr)
    answer.append(nums[-1])
    return answer 

print(findValidElements([1,2,4,2,3,2]))
print(findValidElements([5,5,5,5]))
print(findValidElements([1]))