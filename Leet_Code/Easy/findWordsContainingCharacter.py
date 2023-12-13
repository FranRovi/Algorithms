# Leet Code Algo 2942. Find Words Containing Character

def findWordsContainingCharacter(words, x):
    answer = []
    for i in range(len(words)):
        if x in words[i]:
            answer.append(i)
    return answer

print(findWordsContainingCharacter(["leet", "code"], "e"))
print(findWordsContainingCharacter(["abc", "bdc", "aaaa", "cbc"], "a"))
print(findWordsContainingCharacter(["abc", "bdc", "aaaa", "cbc"], "z"))