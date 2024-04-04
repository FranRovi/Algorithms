# Leet Code Algo 2586. Count the Number of Vowel Strings in Range 

def vowelStrings(words, left, right):
    counter = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(left, right + 1):
        if words[i][0] in vowels and words[i][-1] in vowels:
            counter += 1
    return counter

print(vowelStrings(['are', 'amy', 'u'], 0, 2))
print(vowelStrings(['hey', 'aeo', 'mu', 'ooo', 'artro'], 1, 4)) 