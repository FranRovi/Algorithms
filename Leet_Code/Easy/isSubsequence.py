# Leet Code Algo 392. Is Subsequence.

def isSubsequence(s, t):
    hashSFreq = {}
    hashTFreq = {}
    for char in s:
        if char not in hashSFreq:
            hashSFreq[char] = 1
        else:
            hashSFreq[char] += 1
    for char in t:
        if char not in hashTFreq:
            hashTFreq[char] = 1
        else:
            hashTFreq[char] += 1
    for key, value in hashSFreq.items():
        if key not in hashTFreq or value > hashTFreq[key]:
            return False  
    answer = []
    len_s = len(s)
    ptr = 0
    for i in range(len_s):
        for j in range(ptr, len(t)):
            if s[i] == t[j]:
                answer.append(s[i])
                ptr = j
                break
    return True if len(answer) == len_s else False

print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))
print(isSubsequence("aaaaaa","bbaaaa"))