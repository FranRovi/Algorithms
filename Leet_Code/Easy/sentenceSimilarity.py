# Leet Code Algo 734. Sentence Similarity

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    if sentence1 == sentence2:
        return True
    for i in range(len(sentence1)):
        if [sentence1[i],sentence2[i]] in similarPairs or [sentence2[i],sentence1[i]] in similarPairs:
            continue
        elif sentence1[i] == sentence2[i]:
            for j in range(len(similarPairs)):
                if sentence1[i] == similarPairs[j][0] or sentence1[i] == similarPairs[j][1]:
                    continue
        else:
            return False
    return True

print(areSentencesSimilar(["great","acting","skills"],["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))
print(areSentencesSimilar(["great"],["great"],[]))
print(areSentencesSimilar(["great"], ["doubleplus","good"], [["great","doubleplus"]]))
print(areSentencesSimilar(["great","acting","skills"],["fine","painting","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))
print(areSentencesSimilar(["an","extraordinary","meal"],["one","good","dinner"],[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]))
print(areSentencesSimilar(["one","excellent","meal"],["one","good","dinner"],[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]))  