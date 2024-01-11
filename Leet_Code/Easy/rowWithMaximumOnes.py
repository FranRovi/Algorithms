# Leet Code Algo 2643. Row With Maximum Ones

def rowWithMaximumOnes(mat):
    m = len(mat)
    n = len(mat[0])
    colHash = {}
    for i in range(m):
        colHash[i] = 0
    
    for j in range(m):
        for k in range(n):
            if mat[j][k] == 1:
                colHash[j] += 1
    # print(colHash)
    sortedColHash = sorted(colHash.items(), key= lambda x:x[1], reverse=True)
    sortedHashByFrequency = dict(sortedColHash)
    # print(sortedHashByFrequency)
    for key, val in sortedHashByFrequency.items():
        return[key, val]

print(rowWithMaximumOnes([[0,1], [1,0]]))    
print(rowWithMaximumOnes([[0,0,0], [0,1,1]]))
print(rowWithMaximumOnes([[0,0], [1,1], [0,0]]))