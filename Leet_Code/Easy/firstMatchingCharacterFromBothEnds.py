# Leet Code Algo 3884. First Matching Character From Both Ends.

def firstMatchingIndex(s):
    len_s = len(s)
    right_idx = len_s - 1 
    for i in range(len_s):
        if s[i] == s[right_idx]:
            return i
        right_idx -= 1
    return -1

print(firstMatchingIndex("abcacbd"))
print(firstMatchingIndex("abc"))
print(firstMatchingIndex("abcdab"))