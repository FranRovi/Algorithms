# Leet Code Algo 3662. Filter Characters by Frequency

def filterCharacters(s, k):
    if k == 1:
        return ""
    hash_char_freq = {}
    invalid_chars = []
    for char in s:
        if char not in invalid_chars:
            if char not in hash_char_freq:
                hash_char_freq[char] = 1 
            else:
                temp = hash_char_freq[char] 
                if temp + 1 == k:
                    invalid_chars.append(char)
                    del hash_char_freq[char]  
                else:
                    hash_char_freq[char] += 1
    answer = ""
    for char in s:
        if char in hash_char_freq:
            answer += char
    return answer

print(filterCharacters("aadbbcccca", 3))
print(filterCharacters("xyz", 2))
print(filterCharacters("bcb", 3))
print(filterCharacters("a", 1))