# Leet Code Algo 2210. Count Hills and Valleys in an Array

def countHillValley(nums):
    counter = 0
    nums_no_repeat = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        else:
            nums_no_repeat.append(nums[i])
    for j in range(1, len(nums_no_repeat) -1 ):
        if nums_no_repeat[j] > nums_no_repeat[j-1] and nums_no_repeat[j+1] <  nums_no_repeat[j] or nums_no_repeat[j] < nums_no_repeat[j-1] \
        and nums_no_repeat[j+1] > nums_no_repeat[j]:
            counter += 1
    return counter

print(countHillValley([2,4,1,1,6,5]))
print(countHillValley([6,6,5,5,4,1]))
print(countHillValley([5,7,7,1,7]))
print(countHillValley([21,21,21,2,2,2,2,21,21,45]))  