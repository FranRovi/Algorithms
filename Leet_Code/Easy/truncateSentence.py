# Leet Code Algo 1816. Truncate Sentence

def truncateSentence(s, k):
    sentenceWordsList = s.split(" ")
    truncateSentence = ""
    for i in range(k):
        truncateSentence += sentenceWordsList[i] + " "
    answer = truncateSentence.rstrip()
    return answer

print(truncateSentence("Hello how are you Contestant", 4))
print(truncateSentence("What is the solution to this problem", 4))
print(truncateSentence("Chopper is not a tanuki", 5))