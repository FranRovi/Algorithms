# Leet Code Algo 2351. First Letter To Appear Twice

def firstLetterToAppearTwice(s):
    hashChar = {}
    for i in range(len(s)):
        if s[i] not in hashChar:
            hashChar[s[i]] = 1
        else:
            hashChar[s[i]] += 1
            if hashChar[s[i]] == 2:
                return s[i]

print(firstLetterToAppearTwice("abccbaacz"))
print(firstLetterToAppearTwice("abcdd"))