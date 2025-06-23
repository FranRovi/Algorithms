# Leet Code Algo 3502. Minimum Cost To Reach Every Position

def minCosts(costs):
    lowest_num = costs[0]
    answer = [lowest_num]
    for i in range(1, len(costs)):
        if lowest_num > costs[i]:
            lowest_num = costs[i]
        answer.append(lowest_num)
    return answer

print(minCosts([5,3,4,1,3,2]))
print(minCosts([1,2,4,6,7]))