# Leet Code 35. Search Insert Position

def searchInsertPosition(nums, target):
    if target == 0:
        if nums[0] < 0:
            if nums[1] < 0:
                return 2
            else:
                return 1
        else:
            return 0
    if len(nums) == 2:
        if target <= nums[0]:
            return 0
        elif target > nums[1]:
            return 2
        else:
            return 1
    leftIdx = 0
    rightIdx = len(nums) - 1
    while rightIdx >= leftIdx:
        midVal = round((leftIdx + rightIdx) / 2)
        if nums[midVal] == target:
            return midVal
        elif nums[midVal] < target:
            leftIdx = midVal + 1
        else:
            rightIdx = midVal - 1
    # print(midVal)
    if nums[midVal] <= target:
        return midVal + 1
    else:
        return midVal 

# print(searchInsertPosition([1,3,5,6], 5))
# print(searchInsertPosition([1,3,5,6], 2))
# print(searchInsertPosition([1,3,5,6], 7))
# print(searchInsertPosition([1,3], 2))
# print(searchInsertPosition([1,3,5], 4))
# print(searchInsertPosition([1,3], 1))
# print(searchInsertPosition([-1,3,5,6], 1))
# print(searchInsertPosition([1,3,5,6], 5))
print(searchInsertPosition([-3,-1,3,90], 0))

