# Leet Code Algo 1531. Count Negative Numbers in a Sorted Matrix

def countNegativeNumbersInASortedMatrix(grid):
    counter = 0
    m = len(grid)
    n = len(grid[0])
    # print(size)
    for i in range(m):
        for j in range(n):
            # print(i,j)
            # print(grid[i][j])
            if grid[i][j] < 0:
                counter += 1
    return counter
print(countNegativeNumbersInASortedMatrix([[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2],[-1,-1,-2,-3]]))
print(countNegativeNumbersInASortedMatrix([[3,2], [1,0]]))
print(countNegativeNumbersInASortedMatrix([[5,1,0],[-5,-5,-5]]))
    
