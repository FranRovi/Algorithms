# Leet Code Algo 997. Find the Town Judge

def findJudge(n, trust):
    len_trust = len(trust) 
    if len_trust == 0 and n == 1:
        return 1
    trusted_persons = {}
    citizens = set()
    for i in range(len_trust):
        citizens.add(trust[i][0])
        if trust[i][1] not in trusted_persons:
            trusted_persons[(trust[i][1])] = 1
        else:
            trusted_persons[(trust[i][1])] += 1
    if len(citizens) == n:
        return -1
    max_val = 0
    judge = 0
    for key, value in trusted_persons.items():
        if value > max_val:
            max_val = value
            judge = int(key)
    if max_val + 1 == n:
        return judge
    return -1

print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))
print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(findJudge(3, [[1,2],[2,3]]))
print(findJudge(1, []))