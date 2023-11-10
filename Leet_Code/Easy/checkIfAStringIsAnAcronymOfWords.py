# Leet Code Algo 2828. Check if a string is an Acronym Of Words

def checkIfAStringIsAnAcronymOfWords(words, s):
    # print(len(words), len(s))
    if len(words) != len(s):
        return False
    for i in range(len(words)):
        # print(words[i][0], s[i])
        if words[i][0] != s[i]:
            return False
    return True

print(checkIfAStringIsAnAcronymOfWords(["alice", "bob", "charlie"], 'abc'))
print(checkIfAStringIsAnAcronymOfWords(["an", "apple"], 'a'))
print(checkIfAStringIsAnAcronymOfWords(["never", "gonna","give", "up", "on", "you"], 'ngguoy'))