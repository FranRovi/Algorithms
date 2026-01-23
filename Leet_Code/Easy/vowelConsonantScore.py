# Leet Code Algo 3813. Vowel-Consonant Score

import math

def vowelConsonantScore(s):
    hash_vowels = {"a":1,"e":1,"i":1,"o":1,"u":1}
    hash_consonants = {"b":1,"c":1,"d":1,"f":1,"g":1,"h":1,"j":1,"k":1,"l":1,"m":1,"n":1,"p":1,"q":1,"r":1,"s":1,"t":1,"v":1,"w":1,"x":1,"y":1,"z":1}
    counter_vowels = 0
    counter_consonant = 0
    for char in s:
        if char in hash_vowels:
            counter_vowels += 1
        if char in hash_consonants:
            counter_consonant += 1
    if counter_consonant == 0:
        return 0
    return math.floor(counter_vowels / counter_consonant)

print(vowelConsonantScore("cooear"))
print(vowelConsonantScore("axeyizou"))
print(vowelConsonantScore("au 123"))