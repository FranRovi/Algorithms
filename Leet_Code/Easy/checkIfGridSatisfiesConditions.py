# Leet Code Algo 3142. Check if Grid Satisfies Conditions

def satisfiesConditions(grid):
    row = len(grid)
    col = len(grid[0])

    if col == 1:
        for i in range(1, row):
            if grid[i-1] != grid[i]:
                return False
        return True
    if row == 1:
        for j in range(1, col):
            if grid[0][j-1] == grid[0][j]:
                return False
        return True

    for k in range(1,row):
        for l in range(col):
            if grid[k-1][l] != grid[k][l]:
                return False
    for y in range(row):
        for z in range(1,col):
            if grid[y][z-1] == grid[y][z]:
                return False
    return True

print(satisfiesConditions([[1,0,2],[1,0,2]]))
print(satisfiesConditions([[1,1,1],[0,0,0]]))
print(satisfiesConditions([[1],[2],[3]]))

