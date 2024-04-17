# Hacker Rank Algo Service Lane

def serviceLane(width, cases):
    answer = []
    for i in range(len(cases)):
        tempMin = 100001
        for j in range(cases[i][0], cases[i][1]+1):
            if tempMin > width[j]:
                tempMin = width[j]
        answer.append(tempMin)
    return answer
    
print(serviceLane([2,3,1,2,3,2,3,3], [[0,3],[4,6],[6,7],[3,5],[0,7]]))
print(serviceLane([1,2,2,2,1], [[2,3],[1,4],[2,4],[2,4],[2,3]]))
    