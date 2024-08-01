# Leet Code Algo 1380. Lucky Numbers in a Matrix

def luckyNumbers(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    if rows == 0:
        return []
    if columns == 1:
        largestVal = matrix[0][0]
        for n in range(1, rows):
            if largestVal < matrix[n][0]:
                largestVal = matrix[n][0]
        return [largestVal]    
    highestValsColumns = []
    idxHighestValsRows = []
    highestValCol = 0
    idxHighestValRow = 0     
    for i in range(columns):
        highestValCol = 0
        idxHighestValRow = 0  
        for j in range(rows):
            if highestValCol < matrix[j][i]:
                highestValCol = matrix[j][i]
                idxHighestValRow = j
        highestValsColumns.append(highestValCol)
        idxHighestValsRows.append(idxHighestValRow)
    smallestVal = 100000
    smallestValIdx = 0
    for k in range(len(highestValsColumns)):
        if smallestVal > highestValsColumns[k]:
            smallestVal = highestValsColumns[k]
            smallestValIdx = idxHighestValsRows[k]
    for m in range(len(matrix[smallestValIdx])):
        if matrix[smallestValIdx][m] < smallestVal:
            return []
    return [smallestVal]

    
print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(luckyNumbers([[7,8],[1,2]]))
print(luckyNumbers([[3,6],[7,1],[5,2],[4,8]]))
print(luckyNumbers([[56216],[63251],[75772],[1945],[27014]]))
print(luckyNumbers([[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]))

