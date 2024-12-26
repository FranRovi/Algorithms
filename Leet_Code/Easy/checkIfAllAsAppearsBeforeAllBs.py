# Leet Code Algo 2124. Check If All A's Appears Before All B's

def checkString(s):
    isFirst = True
    firstBIdx = 0
    hashLetters = {
        "a": 0,
        "b": 0
    }
    for i in range(len(s)):
        if s[i] == 'b' and isFirst:
            firstBIdx = i
            isFirst = False
        if s[i] == 'a':
            hashLetters['a'] += 1
        elif s[i] == 'b':
            hashLetters['b'] += 1
    if len(hashLetters) > 0 and hashLetters['b'] == 0:
        return True
    else:
        if hashLetters['a'] > firstBIdx:
            return False
        return True
    
print(checkString("aaabbb"))
print(checkString("abab"))
print(checkString("bbb"))