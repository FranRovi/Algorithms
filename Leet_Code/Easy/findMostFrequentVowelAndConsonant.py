# Leet Code Algo 3541. Find Most Frequent Vowel and Consonant

def maxFreqSum(s):
    hash_vowel = {}
    hash_consonant = {}
    highest_vowel_freq = 0
    highest_consonant_freq = 0
    vowel = ["a", "e", "i", "o", "u"]
    for c in s:
        if c in vowel:
            if c in hash_vowel:
                hash_vowel[c] += 1
                if hash_vowel[c] > highest_vowel_freq:
                    highest_vowel_freq = hash_vowel[c]  
            else:
                hash_vowel[c] = 1
                if hash_vowel[c] > highest_vowel_freq:
                    highest_vowel_freq = 1
        else:
            if c in hash_consonant:
                hash_consonant[c] += 1
                if hash_consonant[c] > highest_consonant_freq:
                    highest_consonant_freq = hash_consonant[c]  
            else:
                hash_consonant[c] = 1
                if hash_consonant[c] > highest_consonant_freq:
                    highest_consonant_freq = 1
    return highest_vowel_freq + highest_consonant_freq

print(maxFreqSum("successes"))
print(maxFreqSum("aeiaeia")) 
print(maxFreqSum("bx")) 
print(maxFreqSum("og"))  