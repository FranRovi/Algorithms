# Leet Code Algo 999. Available Captures for Rook

def numRookCaptures(board):
    rook_pos = [0,0]
    for i in range(8):
        for j in range(8):
            if board[i][j] == "R":
                rook_pos[0] = i
                rook_pos[1] = j
    counter = 0
    for n in range(rook_pos[1], 8, 1):
        if board[n][rook_pos[1]] == "p" or board[n][rook_pos[1]] == "B":
            if board[n][rook_pos[1]] == "p":
                counter += 1
                break
            break
    for m in range(rook_pos[1], -1, -1):
        if board[m][rook_pos[1]] == "p" or board[m][rook_pos[1]] == "B":
            if board[m][rook_pos[1]] == "p":
                counter += 1
                break
            break
    for k in range(rook_pos[0], 8, 1):
        if board[rook_pos[0]][k] == "p" or board[rook_pos[0]][k] == "B":
            if board[rook_pos[0]][k] == "p":
                counter += 1
                break
            break
    for l in range(rook_pos[0], -1, -1):
        if board[rook_pos[0]][l] == "p" or board[rook_pos[0]][l] == "B":
            if board[rook_pos[0]][l] == "p":
                counter += 1
                break
            break
    return counter

print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))  