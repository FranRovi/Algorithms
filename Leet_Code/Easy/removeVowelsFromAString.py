# Leet Code Algo 1119. Remove Vowels From A String

def removeVowels(s):
    vowels = ['a','e','i','o','u']
    answer = ""
    for char in s:
        if char not in vowels:
            answer += char
    return answer

print(removeVowels("leetcodeisacommunityforcoders"))
print(removeVowels("aeiou"))