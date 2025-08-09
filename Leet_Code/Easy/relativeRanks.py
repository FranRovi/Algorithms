# Leet Code Algo 506. Relative Ranks

def findRelativeRanks(score):
    hash_score_pos = {}
    for i in range(len(score)):
        hash_score_pos[score[i]] = i
    sorted_hash_by_key = dict(sorted(hash_score_pos.items(), reverse=True))
    sorted_by_idx = list(sorted_hash_by_key.values())
    answer = [0] * len(score)
    idx = 0
    while idx < len(answer):
        if idx <= 2:
            if idx == 0:
                answer[sorted_by_idx[idx]] = "Gold Medal"
            elif idx == 1:
                answer[sorted_by_idx[idx]] = "Silver Medal"
            else:
                answer[sorted_by_idx[idx]] = "Bronze Medal"
        else:
            answer[sorted_by_idx[idx]] = str(idx+1)
        idx += 1
    return answer

print(findRelativeRanks([5,4,3,2,1]))
print(findRelativeRanks([10,3,8,9,4]))