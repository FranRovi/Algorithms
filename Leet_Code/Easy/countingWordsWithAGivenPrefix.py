# Leet Code Algo 2185. Counting Words With a Given Prefix

def prefixCount(words, pref):
    counter = 0
    for i in range(len(words)):
        if words[i][:len(pref)] == pref:
            counter += 1
    return counter

print(prefixCount(['pay', 'attention', 'practice', 'attend'], 'att'))
print(prefixCount(['leetcode', 'win', 'loops', 'success'], 'code'))            