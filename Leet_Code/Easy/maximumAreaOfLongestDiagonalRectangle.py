# Leet Code Algo 3000. Maximum Area of Longest Diagonal Rectangle
import math

def areaOfMaxDiagonal(dimensions):
    max_area = 0
    max_diagonal = 0

    for i in range(len(dimensions)):
        if math.sqrt(dimensions[i][0] * dimensions[i][0] +
        dimensions[i][1] * dimensions[i][1]) > max_diagonal:
            max_diagonal = math.sqrt(dimensions[i][0] * dimensions[i][0] +
            dimensions[i][1] * dimensions[i][1])
            max_area = dimensions[i][0] * dimensions[i][1] 
        elif math.sqrt(dimensions[i][0] * dimensions[i][0] +
        dimensions[i][1] * dimensions[i][1]) == max_diagonal:
            if dimensions[i][0] * dimensions[i][1] > max_area:
                max_area = dimensions[i][0] * dimensions[i][1]
    return max_area

print(areaOfMaxDiagonal([[9,3],[8,6]]))
print(areaOfMaxDiagonal([[3,4],[4,3]]))
print(areaOfMaxDiagonal([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]))
