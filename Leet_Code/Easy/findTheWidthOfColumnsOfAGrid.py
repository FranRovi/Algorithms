# Leet Code Algo 2639. Find the Width of Columns of a Grid

def findColumnWidth(grid):
    row = len(grid)
    col = len(grid[0]) 
    max_val = 0
    answer = []
    for i in range(col):
        for j in range(row):
            temp = 0
            temp = len(str(grid[j][i]))
            if temp > max_val:
                max_val = temp
        answer.append(max_val)
        max_val = 0
    return answer

print(findColumnWidth([[1],[22],[33]]))
print(findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))
print(findColumnWidth([[93,-20,-4],[6,-20,-19]]))
print(findColumnWidth([[31,100,-6],[10,0,68],[-42,-37,-36]]))