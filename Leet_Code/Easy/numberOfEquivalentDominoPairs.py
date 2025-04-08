# Leet Code 1128. Number of Equivalent Domino Pairs

def numberOfEquivalentDominoPairs(dominoes):
    counter = 0
    hash_dominoes = {}
    for i in range(len(dominoes)):
        temp_smallest = (dominoes[i][0],dominoes[i][1]) if dominoes[i][0] < dominoes[i][1] else (dominoes[i][1],dominoes[i][0])
        if str(temp_smallest) not in hash_dominoes:
            hash_dominoes[str(temp_smallest)] = 1
        else:
            hash_dominoes[str(temp_smallest)] += 1
    for key, value in hash_dominoes.items():
        if value > 1:
            counter += int((value * (value - 1)) / 2)
    return counter

    
    # for i in range(len(dominoList) - 1):
    #     for j in range(i+1, len(dominoList)):
    #         if ((dominoList[i][0] == dominoList[j][0] and
    #             dominoList[i][1] == dominoList[j][1]) or
    #             (dominoList[i][0] == dominoList[j][1] and
    #             dominoList[i][1] == dominoList[j][0])):
    #                 counter += 1
                

print(numberOfEquivalentDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(numberOfEquivalentDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))