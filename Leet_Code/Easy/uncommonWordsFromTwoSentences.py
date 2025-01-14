# Leet Code Algo 884. Uncommon Words From Two Sentences

def uncommonFromSentences(s1, s2):
    listOne = s1.split(" ")
    listTwo = s2.split(" ")
    hashWords = {}
    for i in range(len(listOne)):
        if listOne[i] not in hashWords:
            hashWords[listOne[i]] = 1
        else:
            hashWords[listOne[i]] += 1
    for j in range(len(listTwo)):
        if listTwo[j] not in hashWords:
            hashWords[listTwo[j]] = 1
        else:
            hashWords[listTwo[j]] += 1
    answer = []
    for key, value in hashWords.items():
        if value == 1:
            answer.append(key)
    return answer

print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))
print(uncommonFromSentences("s z z z s", "s z ejt"))
