# Leet Code Algo 2965. Find Missing and Repeated Values

def findMissingAndRepeatedValues(grid):
    max_val = 0
    min_val = 999999
    hash_nums = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in hash_nums:
                hash_nums[grid[i][j]] = 1
                if grid[i][j] > max_val:
                    max_val = grid[i][j]
                if grid[i][j] < min_val:
                    min_val = grid[i][j]  
            else:
                hash_nums[grid[i][j]] += 1
    repeated_num = 0
    missing_num = 0
    for i in range(min_val, max_val + 1):
        if i not in hash_nums:
            missing_num = i
        else:
            if hash_nums[i] == 2:
                repeated_num = i
    if missing_num == 0:
        if min_val > 1:
            return [repeated_num, min_val - 1]
        else:
            return [repeated_num, max_val + 1]
    else:
        return [repeated_num, missing_num]

print(findMissingAndRepeatedValues([[1,3],[2,2]]))
print(findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))
print(findMissingAndRepeatedValues([[2,2],[3,4]]))