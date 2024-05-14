# Leet Code Algo 1572. Matrix Diagional sum
import math

def matrixDiagonalSum(mat):
    n = len(mat)
    left = 0
    right = 0
    for i in range(n):
        left += mat[i][i]
        right += mat[i][n-1-i]
    if len(mat) % 2 == 0:
        return left + right
    else:
        return (left + right) - mat[math.floor(n/2)][math.floor(n/2)]
    
print(matrixDiagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(matrixDiagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
print(matrixDiagonalSum([[5]]))
    