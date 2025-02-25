# Leet Code Algo 1165. Single-Row Keyboard

def calculateTime(keyboard, word):
    hash_letters = {}
    for i in range(len(keyboard)):
        hash_letters[keyboard[i]] = i
    timer = hash_letters[word[0]]
    for j in range(len(word) - 1):
        timer += abs(hash_letters[word[j+1]] - hash_letters[word[j]])
    return timer

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))