# Leet Code Algo 3838. Weighted Word Mapping

def mapWordWeights(words, weights):
    hash_weights = {} 
    idx = 0
    for i in range(97,123):
        hash_weights[chr(i)] = weights[idx]
        idx += 1
    hash_mod_to_letter = {
        "25":"a", "24":"b", "23":"c", "22":"d", "21":"e", "20":"f", "19":"g",
        "18":"h", "17":"i", "16":"j", "15":"k", "14":"l", "13":"m", "12":"n", "11":"o", "10":"p", "9":"q", "8":"r", "7":"s", "6":"t", "5":"u", "4":"v", "3":"w", "2":"x", "1":"y", "0":"z"
    }
    answer = ""
    for j in range(len(words)):
        total_sum = 0
        for l in range(len(words[j])):
            total_sum += hash_weights[words[j][l]]
        temp = total_sum % 26
        answer += hash_mod_to_letter[str(temp)]
    return answer

print(mapWordWeights(["abcd","def","xyz"],[5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
print(mapWordWeights(["a","b","c"],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(mapWordWeights(["abcd"],[7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]))