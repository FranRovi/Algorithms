# Leet Code Algo 3121. Count the Number of Special Characters II.

def numberOfSpecialChars(word):
    hash_lower = {}
    hash_upper = {}
    for i in range(len(word)):
        if word[i].islower():
            if word[i] not in hash_lower:
                hash_lower[word[i]] = [i]
            else:
                hash_lower[word[i]].append(i)
        else:
            if word[i] not in hash_upper:
                hash_upper[word[i]] = [i]
            else:
                hash_upper[word[i]].append(i)
    counter = 0        
    for key, value in hash_lower.items():
        if (key.upper() in hash_upper and
            value[-1] < hash_upper[key.upper()][0]):
            counter += 1
    return counter

print(numberOfSpecialChars("aaAbcBC"))
print(numberOfSpecialChars("abc"))
print(numberOfSpecialChars("AbBCab"))
print(numberOfSpecialChars("aaAbBC"))