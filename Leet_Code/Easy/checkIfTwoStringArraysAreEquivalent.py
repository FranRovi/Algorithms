# Leet Code Algo 1662. Check if Two String Arrays are Equivalent

def arrayStringAreEqual(word1, word2):
    str1 = ""
    str2 = ""
    
    for i in range(len(word1)):
        str1 += word1[i]
    for j in range(len(word2)):
        str2 += word2[j]
    if str1 != str2:
        return False
    return True

print(arrayStringAreEqual(["ab", 'c'],["a", 'bc']))
print(arrayStringAreEqual(["a", 'cb'],["a", 'bc']))
print(arrayStringAreEqual(["abc", 'd', 'defg'],["abcddefg"]))
