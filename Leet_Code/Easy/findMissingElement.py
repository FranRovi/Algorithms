# Leet Code Algo 3731. Find Missing Element.

def findMissingElement(nums):
    sorted_nums = sorted(nums)
    missing_nums = []

    for i in range(sorted_nums[0], sorted_nums[-1]+1):
        if i not in sorted_nums:
            missing_nums.append(i)
    return missing_nums

print(findMissingElement([1,4,2,5]))
print(findMissingElement([7,8,6,9]))
print(findMissingElement([5,1]))
    