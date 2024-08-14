# Leet Code Algo 3248. Snake in Matrix

def finalPositionOfSnake(n, commands):
    row = 0
    column = 0
    matrix = []
    
    for i in range(n):
        line = []
        for j in range(n):
            line.append(n * i + j)
        matrix.append(line)
    
    for k in range(len(commands)):
        if commands[k] == "DOWN":
            row += 1
        elif commands[k] == "UP":
            row -= 1
        elif commands[k] == "RIGHT":
            column += 1
        else:
            column -= 1
    
    return matrix[row][column]
        
print(finalPositionOfSnake(2, ["RIGHT", "DOWN"]))
print(finalPositionOfSnake(3, ["DOWN", "RIGHT", "UP"]))