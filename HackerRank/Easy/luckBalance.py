# Hacker Rank Algo. Luck Balance

def luckBalance(k, contests):
    imp_contest = []
    no_impo_contest = []
    
    for i in range(len(contests)):
        if contests[i][1] == 1:
            imp_contest.append(contests[i][0])
        else:
            no_impo_contest.append(contests[i][0])
    sorted_imp_contest = sorted(imp_contest, reverse= True)
    return sum(sorted_imp_contest[:k]) - sum(sorted_imp_contest[k:]) + sum(no_impo_contest)

print(luckBalance(2, [[5, 1], [1, 1], [4, 0]]))
print(luckBalance(3,[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
print(luckBalance(5,[[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18,1], [13, 1]]))
print(luckBalance(2, [[5, 1], [4, 0], [6, 1], [2, 1], [8, 0]]))