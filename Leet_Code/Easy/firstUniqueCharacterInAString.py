# Leet Code Algo 387. First Unique Character in a String

def firstUniqueCharacterInAString(s):
    hashChar = {}
    repeatedChars = set()
    for i in range(len(s)):
        if s[i] not in repeatedChars:
            if s[i] not in hashChar:
                hashChar[s[i]] = i
            else:
                repeatedChars.add(s[i])
                del hashChar[s[i]]
    if len(hashChar) == 0:
        return -1
    else:
        return list(hashChar.items())[0][1]

print(firstUniqueCharacterInAString('leetcode'))
print(firstUniqueCharacterInAString('loveleetcode'))
print(firstUniqueCharacterInAString('aabb'))
print(firstUniqueCharacterInAString('aadadaad'))