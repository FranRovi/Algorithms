# Leet Code Algo 3913. Sort Vowels by Frequency

def sortVowels(s):
    vowels = {"a": 1,"e": 1,"i": 1,"o": 1,"u": 1}
    freq_vowels_hash = {}
    for char in s:
        if char in vowels:
            if char in freq_vowels_hash:
                freq_vowels_hash[char] += 1
            else:
                freq_vowels_hash[char] = 1
    sorted_freq_hash = dict(sorted(freq_vowels_hash.items(), key =lambda item:item[1], reverse=True))
    sorted_vowels = []
    for key, value in sorted_freq_hash.items():
        for i in range(value):
            sorted_vowels.append(key)
    idx = 0 
    s_list = list(s)
    len_s_list = len(s_list)
    if len_s_list == len(sorted_vowels):
        return "".join(sorted_vowels)
    for j in range(len(s_list)):
        if s_list[j] in vowels:
            s_list[j] = sorted_vowels[idx]
            idx += 1
    return "".join(s_list)

print(sortVowels("leetcode"))
print(sortVowels("aeiaaioooa"))
print(sortVowels("baeiou"))