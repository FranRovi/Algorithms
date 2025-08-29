# Leet Code Algo 2022. Convert 1D Array Into 2D Array

def construct2DArray(original, m, n):
    arr_len = len(original)
    matrix = []
    if m == 1 and n < arr_len:
        return []
    elif m == 1 and n == arr_len:
        return [original]
    elif m * n == arr_len:
        idx = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[idx])
                idx += 1
            matrix.append(temp)
    return matrix

print(construct2DArray([1,2,3,4],2,2))
print(construct2DArray([1,2,3],1,3))
print(construct2DArray([1,2],1,1))