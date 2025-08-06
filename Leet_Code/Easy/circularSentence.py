# Leet Code Algo 2490. Circular Sentence

def isCircularSentence(sentence):
    arr_words = sentence.split(" ")
    if len(arr_words) == 1:
        if arr_words[0][0] == arr_words[0][-1]:
            return True
    for i in range(len(arr_words)-1):
        if arr_words[i][-1] != arr_words[i+1][0]:
            return False
    if arr_words[len(arr_words)-1][-1] == arr_words[0][0]:
            return True
    else:
        return False
    
print(isCircularSentence("leetcode exercises sound delightful"))
print(isCircularSentence("eetcode"))
print(isCircularSentence("Leetcode is cool"))