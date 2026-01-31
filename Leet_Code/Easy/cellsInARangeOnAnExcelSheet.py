# Leet Code Algo 2194. Cells in a Range on an Excel Sheet

def cellsInRange(s):
    row_start = ord(s[1])
    row_end = ord(s[4])
    col_start = ord(s[0]) 
    col_end = ord(s[3])

    answer = []
    for j in range(int(col_start), int(col_end)+1):
        for i in range(int(row_start), int(row_end)+1):
            temp = chr(j) + chr(i)
            answer.append(temp)
    return answer
    
print(cellsInRange("K1:L2"))
print(cellsInRange("A1:F1"))