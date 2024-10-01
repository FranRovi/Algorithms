# Leet Code Algo 2733. Neither Minimum or Maximum

def findNorMinOrMax(nums):
    if len(nums) <= 2:
        return -1
    smaller = nums[0]
    larger = nums[0]
    for i in range(len(nums)):
        if nums[i] > larger:
            larger = nums[i]
        if nums[i] < smaller:
            smaller = nums[i]
    for j in range(len(nums)):
        if nums[j] != smaller and nums[j] != larger:
            return nums[j]

print(findNorMinOrMax([3,2,1,4]))
print(findNorMinOrMax([1,2]))
print(findNorMinOrMax([2,1,3]))