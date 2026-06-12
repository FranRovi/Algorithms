# Leet Code Algo 3024. Type of Triangle

def triangleType(nums):
    if (nums[0] + nums[1] <= nums[2] or
        nums[1] + nums[2] <= nums[0] or
        nums[0] + nums[2] <= nums[1]):
        return "none"
    if nums[0] == nums[1] and nums[1] == nums[2]:
        return "equilateral"
    if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
        return "isosceles"
    return "scalene"

print(triangleType([3,3,3]))
print(triangleType([3,4,5]))
print(triangleType([3,3,4]))
print(triangleType([3,4,10]))
print(triangleType([2,7,7]))
print(triangleType([8,4,4]))