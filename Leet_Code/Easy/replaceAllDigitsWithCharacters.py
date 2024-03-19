# Leet Code Algo 1844. Replace all Digits with Characters

def replaceAllDigitsWithCharacters(s):
    answer = ""
    for i in range(len(s)):
        if i % 2 == 0:
            answer += s[i]
        else:
            prevUni = (ord(s[i -1]))
            currUni = (int(s[i])) + prevUni
            currChar = chr(currUni)
            answer += currChar
    return answer
            

print(replaceAllDigitsWithCharacters("a1c1e1"))
print(replaceAllDigitsWithCharacters("a1b2c3d4e"))