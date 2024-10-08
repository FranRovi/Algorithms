# Leet Code Algo 448. Find All Numbers Disappeared in an Array

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    answer = []
    setNums = set(nums)
    for i in range(1, len(nums) +1):
        if i not in setNums:
            answer.append(i)
    return answer

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))

