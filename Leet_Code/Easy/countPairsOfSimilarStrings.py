# Leet Code Algo 2506. Count Pairs Of Similar Strings

def similarPairs(words):
    counter = 0
    for i in range(len(words) -1):
        for j in range(i+1, len(words)):
            if set(words[i]) == set(words[j]):
                counter += 1
    return counter

print(similarPairs(["aba","aabb","abcd","bac","aabc"]))
print(similarPairs(["aabb","ab","ba"]))
print(similarPairs(["nba","cba","dba"]))