# Leet Code Algo 2114. Maximum Number of Words Found in Sentences

def maximumNumberOfWordsFoundInSentences(sentences):
    answer = 0
    for i in range(len(sentences)):
        sentenceList = sentences[i].split(" ")
        # print(sentenceList)
        counter = 0
        for j in range(len(sentenceList)):
            counter += 1
        if counter > answer:
            answer = counter
    return answer
print(maximumNumberOfWordsFoundInSentences(["alice and bob love leetcode", "I think so too", "this is great thanks very much"]))
            
            
            