# Leet Code Algo 2248. Intersection of Multiple Arrays

def intersection(nums):
    hash_nums = {}
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] not in hash_nums:
                hash_nums[nums[i][j]] = 1
            else:
                hash_nums[nums[i][j]] += 1
    answer = []
    for key, value in hash_nums.items():
        if value == len(nums):
            answer.append(key)
    return sorted(answer)

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(intersection([[1,2,3],[4,5,6]]))