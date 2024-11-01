# Leet Code Algo 1935. Maximum Number Of Words You Can Type

def canBeTypedWords(text, brokenLetters):
    counter = 0
    textList = text.split(" ")
    for i in range(len(textList)):
        for j in range(len(brokenLetters)):
            if brokenLetters[j] not in textList[i]:
                continue
            else:
                counter += 1
                break
    return len(textList) - counter

print(canBeTypedWords("hello world","ad"))
print(canBeTypedWords("leet code","lt"))
print(canBeTypedWords("leet code","e"))