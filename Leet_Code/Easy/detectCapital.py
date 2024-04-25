# Leet Code Algo 520. Detect Capital

def detectCapital(word):
    if word.islower() == True:
        return True
    if word.isupper() == True:
        return True
    if word[0].isupper() == True and word[1:].islower() == True:
        return True
    return False

print(detectCapital("USA"))
print(detectCapital("FlaG")) 