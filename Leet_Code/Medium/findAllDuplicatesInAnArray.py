# Leet Code Algo 442. Find All Duplicates in an Array

def findDuplicates(nums):
    answer = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            answer.append(abs(nums[i]))
        else:
            nums[index] = nums[index] * - 1 
    return answer

print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([1,1,2]))
print(findDuplicates([]))
print(findDuplicates([10,2,5,10,9,1,1,4,3,7]))