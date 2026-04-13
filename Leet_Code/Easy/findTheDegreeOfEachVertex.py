# Leet Code Algo 3898. Find the Degree of Each Vertex

def findDegree(matrix):
    hash_degrees = {}
    mat_len = len(matrix)
        
    for i in range(mat_len):
        hash_degrees[i] = 0

    for j in range(mat_len):
        for k in range(mat_len):
            if matrix[j][k] == 1:
                hash_degrees[j] += 1
    return list(hash_degrees.values())

print(findDegree([[0,1,1],[1,0,1],[1,1,0]]))
print(findDegree([[0,1,0],[1,0,0],[0,0,0]])) 
print(findDegree([[0]]))  