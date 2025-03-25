# Leet Code Algo 3238. Find the Number of Winning Players

def winningPlayerCount(n, pick):
    hash_players = {}
    for i in range(n):
        hash_players[i] = {}
    for j in range(len(pick)):
            if pick[j][0] in hash_players:
                if pick[j][1] in hash_players[pick[j][0]]:
                    hash_players[pick[j][0]][pick[j][1]] += 1
                else:
                    hash_players[pick[j][0]][pick[j][1]] = 1
    winning_players = set()
    counter = 0
    for key in hash_players.keys():
        for k, v in hash_players[key].items():
            if v >= key + 1:
                counter += 1
                winning_players.add(key)  
    return len(winning_players)

print(winningPlayerCount(4, [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))
print(winningPlayerCount(5, [[1,1],[1,2],[1,3],[1,4]]))
print(winningPlayerCount(5, [[1,1],[2,4],[2,4],[2,4]]))
    