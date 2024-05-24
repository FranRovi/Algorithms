# Leet Code Algo 1832. Check if Sentence is a Pangram

def checkIsPangram(sentence):
    counter = 0
    hashLetters = {}
    for i in range(len(sentence)):
        if sentence[i].isalpha() and sentence[i] not in hashLetters:
            counter += 1
            hashLetters[sentence[i]] = 1
    if counter > 25:
        return True
    else:
        return False
    
print(checkIsPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIsPangram("leetcode"))
    