# Leet Code Algo 2057. Smallest Index With Equal Value

def smallestEqual(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

print(smallestEqual([0,1,2]))
print(smallestEqual([4,3,2,1]))
print(smallestEqual([1,2,3,4,5,6,7,8,9,0]))
