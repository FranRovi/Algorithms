# Leet Code Algo 1817. Finding the Users Active Minutes

def findingUsersActiveMinutes(logs, k):
    hash_id = {}
    for i in range(len(logs)):
        if logs[i][0] not in hash_id:
            hash_id[logs[i][0]] = [logs[i][1]]
        else:
            hash_id[logs[i][0]].append(logs[i][1])
    hash_freq = {}
    for key, value in hash_id.items():
        len_temp_set = len(set(value))
        if len_temp_set not in hash_freq:
            hash_freq[len_temp_set] = 1
        else:
            hash_freq[len_temp_set] += 1
    answer = [0] * k
    for key, value in hash_freq.items():
        answer[key -1] = value
    return answer

print(findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))
print(findingUsersActiveMinutes([[1,1],[2,2],[2,3]], 4))


    