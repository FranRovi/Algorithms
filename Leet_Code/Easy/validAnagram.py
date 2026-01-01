# Leet Code Algo 242. Valid Anagram

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hash_s = {}
    for char in s:
        if char not in hash_s:
            hash_s[char] = 1
        else:
            hash_s[char] += 1
    hash_t = {}
    for char in t:
        if char not in hash_t:
            hash_t[char] = 1
        else:
            hash_t[char] += 1
    for key, value in hash_s.items():
        if key not in hash_t or value != hash_t[key]:
            return False
    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat", "cat"))
print(isAnagram("a", "ab"))