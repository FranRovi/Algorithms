# Leet Code Algo 1436. Destination City

def destCity(paths):
    hash_paths = {}
    for i in range(len(paths)):
        if paths[i][0] not in hash_paths:
            hash_paths[paths[i][0]] = [1, 0]
        else:
            hash_paths[paths[i][0]] += 1
    for j in range(len(paths)):
        if paths[j][1] not in hash_paths:
            hash_paths[paths[j][1]] = [0,1]
        else:
            hash_paths[paths[j][1]][1] += 1
    for key, value in hash_paths.items():
        if value[0] == 0 and value[1] == 1:
            return key

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))
print(destCity([["A","Z"]]))
