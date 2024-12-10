# Leet Code Algo 389. Find The Difference

def findTheDifference(s, t):
    sHashLetter = {}
    for i in range(len(s)):
        if s[i] not in sHashLetter:
            sHashLetter[s[i]] = 1
        else:
            sHashLetter[s[i]] += 1
    tHashLetter = {}
    for j in range(len(t)):
        if t[j] not in tHashLetter:
            tHashLetter[t[j]] = 1
        else:
            tHashLetter[t[j]] += 1
    for key, value in tHashLetter.items():
        if key not in sHashLetter or value > sHashLetter[key]:
            return key
    
print(findTheDifference('abcd', 'abcde'))
print(findTheDifference('', 'y'))

