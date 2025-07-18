# Leet Code Algo 1160. Find Words That Can Be Formed by Characters

from itertools import permutations

def countCharacters(words, chars):
    hash_chars = {}
    answer = 0
    for c in chars:
        if c not in hash_chars:
            hash_chars[c] = 1
        else:
            hash_chars[c] += 1
    for i in range(len(words)):
        temp_hash = {}
        for j in range(len(words[i])):
            if words[i][j] not in temp_hash:
                temp_hash[words[i][j]] = 1
            else:
                temp_hash[words[i][j]] += 1
        temp_str = ""
        for key, value in temp_hash.items():
            if key in hash_chars and value <= hash_chars[key]:
                temp_str += key * value
            else:
                break
        if len(temp_str) == len(words[i]):
            answer += len(words[i])
            temp_str = ""
    return answer
    
print(countCharacters(["cat","bt","hat","tree"], "atach"))
print(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))

