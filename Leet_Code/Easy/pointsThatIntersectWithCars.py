# Leet Code Algo 2848. Points That Intersect With Cars

def pointsThatIntersectWithCars(nums):
    answer = set()
    for i in range(len(nums)):
        for j in range(nums[i][0], nums[i][1] + 1):
            answer.add(j)
    return len(answer)

print(pointsThatIntersectWithCars([[3,6], [1,5], [4,7]]))
print(pointsThatIntersectWithCars([[1,3], [5,8]]))