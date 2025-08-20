# Leet Code Algo 2923. Find Champion I

def findChampion(grid):
    hash_player_wins = {}
    counter = 0
    winner = -1
    max_wins = -1
    num_players = len(grid[0])
    for i in range(len(grid)):
        for j in range(num_players):
            if i == j:
                continue
            else:
                if grid[i][j] == 1:
                    counter += 1
        hash_player_wins[i] = counter
        if counter > max_wins:
            max_wins = counter
            winner = i
        counter = 0
    return winner

print(findChampion([[0,1],[0,0]]))
print(findChampion([[0,0,1],[1,0,1],[0,0,0]]))