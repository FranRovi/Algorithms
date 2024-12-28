# Leet Code Algo 1876. Substrings of Size Three With Distinct Characters

def countGoodStrings(s):
    counter = 0
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
            counter += 1
    return counter

print(countGoodStrings("xyzzaz"))
print(countGoodStrings("aababcabc"))


  