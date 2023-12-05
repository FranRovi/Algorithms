# Leet Code Algo 1859. Sorting the Sentence

def sortSentence(s):
    s = s.replace(',', '')
    splitSentence = s.split(' ')
    answer = ""
    hashOrderedWord = {}
    
    for i in range(len(splitSentence)):
        activeWord = splitSentence[i]
        idx = activeWord[-1]
        activeWordNoIdx = activeWord[:len(activeWord)-1]
        hashOrderedWord[idx] = activeWordNoIdx
    
    for j in range(1, len(s)):
        if str(j) in hashOrderedWord:
            answer += hashOrderedWord[str(j)] + " "
    answer = answer.rstrip()
    return answer
    
print(sortSentence("is2 sentence4 This1 a3"))    
print(sortSentence("Myself2, Me1, I4 and3"))
