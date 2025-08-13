# Leet Code Algo 1408. String Matching in an Array

def stringMatching(words):
    sorted_words = sorted(words, key=len)
    len_sorted = len(sorted_words)
    answer = set()
    for i in range(len_sorted):
        for j in range(i+1, len(sorted_words)):
            if sorted_words[i] in sorted_words[j]:
                if sorted_words[i] != sorted_words[j]:
                    answer.add(sorted_words[i])
    return list(answer)

print(stringMatching(["mass","as","hero","superhero"]))
print(stringMatching(["leetcode","et","code"]))
print(stringMatching(["blue", "green", "bu"]))
print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))