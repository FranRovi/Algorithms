# Leet Code Algo 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

def isPrefixOfWord(sentence, searchWord):
    list_sentence = sentence.split(" ")
    for i in range(len(list_sentence)):
        if len(list_sentence[i]) >= len(searchWord) and searchWord == list_sentence[i][:len(searchWord)]: 
            return i + 1
    return -1

print(isPrefixOfWord("i love eating burger", "burg"))
print(isPrefixOfWord("this problem is an easy problem", "pro"))
print(isPrefixOfWord("i am tired", "you"))
print(isPrefixOfWord("hellohello hellohellohello", "ell")) 