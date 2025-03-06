# Leet Code Algo 1337. The K Weakest Rows in a Matrix

def kweakestRows(mat, k):
    hash_soldiers = {}
    soldiers_tuple_arr = []
    for i in range(len(mat)):
        count_soldiers = 0
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count_soldiers += 1
            else:
                break
        hash_soldiers[i] = count_soldiers
    for key, value in hash_soldiers.items():
        soldiers_tuple_arr.append((key, value))
    sorted_soldiers_tuple_arr = sorted(soldiers_tuple_arr, key = lambda x:x[1])
    answer = []
    for l in range(k):
        answer.append(sorted_soldiers_tuple_arr[l][0])
    return answer

print(kweakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
print(kweakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2))
print(kweakestRows([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]],1))
print(kweakestRows([[1,0],[1,0],[1,0],[1,1]],4))
print(kweakestRows([[1,0],[0,0],[1,0]],2))