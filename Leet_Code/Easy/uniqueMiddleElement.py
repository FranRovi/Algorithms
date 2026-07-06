# Leet Code Algo 3978. Unique Middle Element 

def isMiddleElementUnique(nums):
    mid_val = len(nums) // 2
    target = nums[mid_val]
    counter = 0
    for n in nums:
        if n == target:
            counter += 1
    if counter == 1:
        return True
    return False

print(isMiddleElementUnique([1,2,3]))
print(isMiddleElementUnique([1,2,2]))