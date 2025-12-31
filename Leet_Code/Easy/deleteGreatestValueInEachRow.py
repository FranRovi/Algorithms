# Leet Code Algo 2500. Delete Greatest Value in Each Row

def deleteGreatestValue(grid):
    if len(grid) == 1:
        return sum(grid[0])
    
    total_sum = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        grid[i] = sorted(grid[i], reverse=True)
    temp_max = 0
    for j in range(n):
        for k in range(m):
            if grid[k][j] > temp_max:
                temp_max = grid[k][j]
        total_sum += temp_max
        temp_max = 0
    return total_sum
    
print(deleteGreatestValue([[1,2,4],[3,3,1]]))
print(deleteGreatestValue([[10]]))
print(deleteGreatestValue([[9,81],[33,17]]))