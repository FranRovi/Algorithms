# Leet Code Algo 2273. Find Resultant Array After Removing Anagrams

def removeAnagrams(words):
    answer = [words[0]]
    for i in range(1, len(words)):
        temp_dict_one = {}
        temp_dict_two = {}
        for j in range(len(words[i])):
            if words[i][j] not in temp_dict_one:
                temp_dict_one[words[i][j]] = 1
            else:
                temp_dict_one[words[i][j]] += 1
        for k in range(len(words[i-1])):
            if words[i-1][k] not in temp_dict_two:
                temp_dict_two[words[i-1][k]] = 1
            else:
                temp_dict_two[words[i-1][k]] += 1
        if temp_dict_one != temp_dict_two:
            answer.append(words[i])
    return answer

print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print(removeAnagrams(["a","b","c","d","e"]))