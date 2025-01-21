# Leet Code Algo 2068. Check Whether Two Strings are Almost Equivalent

def checkAlmostEquivalent(word1, word2):
    hashWordOne = {}
    for char in word1:
        if char not in hashWordOne:
            hashWordOne[char] = 1
        else:
            hashWordOne[char] += 1
    hashWordTwo = {}
    for char in word2:
        if char not in hashWordTwo:
            hashWordTwo[char] = 1
        else:
            hashWordTwo[char] += 1
    diff_words = []
    for char in word2:
        if char not in word1:
            hashWordOne[char] = 0
    for key, value in hashWordOne.items():
        if key not in hashWordTwo and value > 3:
            return False
        elif key in hashWordTwo and abs(value - hashWordTwo[key])  > 3:
            return False
    return True

print(checkAlmostEquivalent("aaaa","bccb"))
print(checkAlmostEquivalent("abcdeef","abaaacc"))
print(checkAlmostEquivalent("cccddabba","babababab"))
print(checkAlmostEquivalent("aaaa","aaaa"))
