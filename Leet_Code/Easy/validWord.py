# Leet Code Algo 3136. Valid Word

def isValid(word):
    counterVowels = 0
    counterConsonants = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    if len(word) < 3:
        return False
    for i in range(len(word)):
        if word[i].isalpha() and word[i] in vowels:
            counterVowels += 1
        elif word[i].isalpha() and word[i] not in vowels:
            counterConsonants += 1
        elif word[i].isdigit():
            continue
        else:
            return False
    if counterVowels > 0 and counterConsonants > 0:
        return True
    else:
        return False

print(isValid("234Adas"))
print(isValid("b3"))
print(isValid("a3$e"))
print(isValid("e4"))