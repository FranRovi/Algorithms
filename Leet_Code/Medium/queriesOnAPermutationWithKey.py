# Leet Code Algo 1409. Queries on a Permutation With Key.

def processQueries(queries, m):
    perm = []
    for i in range(m):
        perm.append(i+1)
    len_queries = len(queries)
    answer = [0] * len_queries
    for j in range(len_queries):
        temp = perm.index(queries[j])
        answer[j] = temp
        perm = [queries[j]] + perm[:temp] + perm[temp+1:]
    return answer
    
print(processQueries([3,1,2,1], 5))
print(processQueries([4,1,2,2], 4))
print(processQueries([7,5,5,8,3], 8))