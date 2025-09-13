# Leet Code Algo 2287. Rearrange Characters to Make Target String

def rearrangeCharacters(s, target):
    if len(target) > len(s):
        return 0
    hash_target = {}
    hash_s = {}
    for i in range(len(target)):
        if target[i] not in hash_target:
            hash_target[target[i]] = 1
        else:
            hash_target[target[i]] += 1
    for j in range(len(s)):
        if s[j] not in hash_s:
            hash_s[s[j]] = 1
        else:
            hash_s[s[j]] += 1
    matches = []
    for key, value in hash_target.items():
        if key in hash_s:
            matches.append(hash_s[key] // value)
        else:
            return 0
    if len(matches) == 0:
        return 0
    else:
        return min(matches)

print(rearrangeCharacters("ilovecodingonleetcode", "code"))
print(rearrangeCharacters("abcba", "abc"))
print(rearrangeCharacters("abbaccaddaeea", "aaaaa"))
print(rearrangeCharacters("abc", "abcd"))
print(rearrangeCharacters("zys", "adk"))
print(rearrangeCharacters("wvu", "tu"))