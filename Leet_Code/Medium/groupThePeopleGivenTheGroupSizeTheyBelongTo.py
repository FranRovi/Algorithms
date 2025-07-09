# Leet Code Algo 1282. Group The People Given the Group Size They Belong To

def groupThePeople(groupSizes):
    hash_groups = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] not in hash_groups:
            hash_groups[groupSizes[i]] = [i]
        else:
            hash_groups[groupSizes[i]].append(i)
    answer = []
    for key, value in hash_groups.items():
        if key == len(value):
            answer.append(value)
        else:
            temp = []
            idx = -1
            for j in range(len(value)):
                if j % key == 0:
                    idx += 1
                    temp.append([value[j]])
                    
                else:
                    temp[idx].append(value[j])
            for arr in temp:
                answer.append(arr)
    return answer

print(groupThePeople([3,3,3,3,3,1,3]))
print(groupThePeople([2,1,3,3,3,2]))