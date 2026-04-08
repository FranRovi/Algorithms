# Leet Code Algo 3773. Maximum Number of Equal Length Runs

def maxSameLengthRuns(s):
    hash_runs = {}
    temp = s[0]
    for i in range(1, len(s)):
        if temp[-1] == s[i]:
            temp += s[i]
        else:
            if temp not in hash_runs:
                hash_runs[temp] = 1
            else:
                hash_runs[temp] += 1
            temp = s[i]
    if temp not in hash_runs:
        hash_runs[temp] = 1
    else:
        hash_runs[temp] += 1
    hash_len = {}
    for key, value in hash_runs.items():
        if len(key) not in hash_len:
            hash_len[len(key)] = value
        else:
            hash_len[len(key)] += value
    max_val = 0
    for key, value in hash_len.items():
        if value > max_val:
            max_val = value
    return max_val

print(maxSameLengthRuns("hello"))
print(maxSameLengthRuns("aaabaaa"))
print(maxSameLengthRuns("abab"))