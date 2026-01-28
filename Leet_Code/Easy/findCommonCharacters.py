# Leet Code ALgo 1002. Find Common Characters

def commonChars(words):
    if len(words) == 1:
        answer = []
        for char in words[0]:
            answer.append(char)
        return answer
    hash_word_one = {}
    hash_word_two = {}
    for char in words[0]:
        if char not in hash_word_one:
            hash_word_one[char] = 1
        else:
            hash_word_one[char] += 1
    for char in words[1]:
        if char not in hash_word_two:
            hash_word_two[char] = 1
        else:
            hash_word_two[char] += 1
    hash_solution = {}
    for key, value in hash_word_two.items():
        if key in hash_word_one:
            if value <= hash_word_one[key]:
                hash_solution[key] = value
            else:
                hash_solution[key] = hash_word_one[key]
    hash_sol_elem = len(hash_solution)
    len_words = len(words)
    for i in range(2, len_words):
        temp_hash = {}
        keys_to_del = []
        for j in range(len(words[i])):
            if words[i][j] not in temp_hash:
                temp_hash[words[i][j]] = 1
            else:
                temp_hash[words[i][j]] += 1
        for key, value in hash_solution.items():
            if key in temp_hash:
                if temp_hash[key] < value:
                    hash_solution[key] = temp_hash[key]
            else:
                keys_to_del.append(key)
        len_keys_to_del = len(keys_to_del)
        hash_sol_elem -= len_keys_to_del
        if hash_sol_elem == 0:
            return []
        for k in range(len_keys_to_del):
            del hash_solution[keys_to_del[k]]
    answer = []
    for key, value in hash_solution.items():
        for l in range(value):
            answer.append(key)
    return answer

print(commonChars(["bella","label","roller"]))
print(commonChars(["cool","lock","cook"]))
print(commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))
print(commonChars(["cool"]))
    