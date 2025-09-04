# Leet Code Algo 2225. Find Players With Zero or One Losses

def findWinners(matches):
    hash_players = {}
    for i in range(len(matches)):
        if matches[i][0] not in hash_players:
            hash_players[matches[i][0]] = [1,0]
        else:
            hash_players[matches[i][0]][0] += 1
        if matches[i][1] not in hash_players:
            hash_players[matches[i][1]] = [0,1]
        else:
            hash_players[matches[i][1]][1] += 1
    answer = [[],[]]
    for key, value in hash_players.items():
        if value[1] == 0:
            answer[0].append(key)
        elif value[1] == 1:
            answer[1].append(key)
    sorted_winners = sorted(answer[0])
    sorted_one_loss = sorted(answer[1])
        
    answer[0] = sorted_winners
    answer[1] = sorted_one_loss 
    return answer

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))  