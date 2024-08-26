# Leet Code 747. Largest Number At Least Twice of Others

def dominantIndex(nums):
    largest = nums[0]
    largestIdx = 0
    for i in range(1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            largestIdx = i
    for j in range(len(nums)):
        if j == largestIdx:
            continue
        elif nums[j] * 2 > largest:
            return -1
    return largestIdx

print(dominantIndex([3,6,1,0]))
print(dominantIndex([1,2,3,4])) 