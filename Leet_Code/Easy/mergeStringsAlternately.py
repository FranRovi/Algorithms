# Leet Code 1768. Merge Strings Alternately

def mergeStringsAlternately(word1, word2):
    mergedString = ''
    shortestWord = word1 if len(word1) < len(word2) else word2
    for i in range(len(shortestWord)):
        mergedString += word1[i] + word2[i]
    if shortestWord == word1:
        for j in range(len(word1), len(word2)):
            mergedString += word2[j]
    else:
        for k in range(len(word2), len(word1)):
            mergedString += word1[k]
    return mergedString

print(mergeStringsAlternately('abc','pqr'))
print(mergeStringsAlternately('ab','pqrs'))
print(mergeStringsAlternately('abcd','pq'))
