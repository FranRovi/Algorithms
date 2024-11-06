# Leet Code Algo 867. Transpose Matrix

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    answer = [[0 for j in range(n)] for i in range(m)]
    if n == m:    
        for i in range(n):
            for j in range(m):              
                answer[i][j] = matrix[j][i]
    else:       
        for i in range(n):
            for j in range(m):             
                answer[j][i] = matrix[i][j]
    return answer
    
print(transpose([[2,4,-1],[-10,5,11],[18,-7,6]]))
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))