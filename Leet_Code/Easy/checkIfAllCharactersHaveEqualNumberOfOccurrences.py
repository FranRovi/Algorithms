# Leet Code Algo 1941. Check if All Characters Have Equal Number Of Occurrences

def areOccurrencesEqual(s):
    hashChars = {}
    for c in s:
        if c not in hashChars:
            hashChars[c] = 1
        else:
            hashChars[c] += 1
    answer = set()
    for item in hashChars.items():
        answer.add(item[1])
    if len(answer) <= 1:
        return True
    return False

print(areOccurrencesEqual('abacbc'))
print(areOccurrencesEqual('aaabb'))