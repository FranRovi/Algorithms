# Leet Code Algo 3210. Count the Number of Special Characters I

def numberOfSpecialChars(word):
    hashCharsLower = {}
    hashCharsUpper = {}
    counter = 0
    for i in range(len(word)):
        if word[i].islower():
            if word[i] not in hashCharsLower:
                hashCharsLower[word[i]] = 1
            else:
                hashCharsLower[word[i]] += 1
        else:
            if word[i] not in hashCharsUpper:
                hashCharsUpper[word[i]] = 1
            else:
                hashCharsUpper[word[i]] += 1
    for key, value in hashCharsLower.items():
        if key.upper() in hashCharsUpper:
            counter += 1
    return counter

print(numberOfSpecialChars("aaAbcBC"))
print(numberOfSpecialChars("abc"))
print(numberOfSpecialChars("abBCab"))