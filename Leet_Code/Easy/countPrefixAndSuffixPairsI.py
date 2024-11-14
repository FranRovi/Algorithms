# Leet Code Algo 3042. Count Prefix and Suffix Pairs I

def countPrefixSuffixPairs(words):
    counter = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if len(words[i]) > len(words[j]):
                continue
            else:
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    counter += 1
    return counter

print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(countPrefixSuffixPairs(["abab","ab"]))