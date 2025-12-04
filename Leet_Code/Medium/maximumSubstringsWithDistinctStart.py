# Leet Code Algo 3760. Maximum Substrings With Distinct Start

def maxDistinct(s):
    return len(set(s))

    # hash_char = {}
    # for char in s:
    #     if char not in hash_char:
    #         hash_char[char] = 1
    # return len(hash_char)
print(maxDistinct("abab"))
print(maxDistinct("abcd"))
print(maxDistinct("aaaa"))