# Leet Code Algo 3033. Modify the Matrix

def modifyTheMatrix(matrix):
    tempLargest = 0
    tempNegativeX = []
    tempNegativeY = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[j][i] > tempLargest:
                tempLargest = matrix[j][i]
            if matrix[j][i] == -1:
                tempNegativeX.append(j)
                tempNegativeY.append(i)
        if len(tempNegativeX) >= 1:
            for k in range(len(tempNegativeX)):
              matrix[tempNegativeX[k]][tempNegativeY[k]] = tempLargest  
        tempLargest = 0
        tempNegativeX = []
        tempNegativeY = []
    return matrix
                          
print(modifyTheMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))
print(modifyTheMatrix([[3,-1],[5,2]]))
print(modifyTheMatrix([[-1,0,0,2,2],[2,0,0,2,1],[4,3,2,1,1],[-1,-1,0,2,4],[1,0,3,-1,0]]))
print(modifyTheMatrix([[2,-1,2,-1,2],[1,0,-1,2,-1],[2,-1,-1,-1,2],[2,1,2,-1,2],[0,1,0,0,0],[0,0,0,0,-1],[2,-1,2,2,0],[0,1,0,2,2],[2,2,0,1,-1]]))