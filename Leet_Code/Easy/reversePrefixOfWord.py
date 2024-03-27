# Leet Code Algo 2000. Reverse Prefix of Word

def reversePrefixOfWord(word, ch):
    answer = ""
    charPos = -1
    for i in range(len(word)):
        if word[i] == ch:
            charPos = i
            break
    for j in range(charPos, -1, -1):
        answer += word[j]
    for k in range(charPos + 1, len(word)):
        answer += word[k]
    return answer
print(reversePrefixOfWord("abcdefd", "d"))
print(reversePrefixOfWord("xyxzxe", "z"))
print(reversePrefixOfWord("abcd", "z"))