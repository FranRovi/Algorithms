# Leet Code 345. Reverse Vowels of a String

def reverseVowelsOfAString(s):
    vowelsArr = []
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    reverseStr = ''
    for i in range(len(s)):
        if s[i] in vowels:
            vowelsArr.append(s[i])
    pointer = len(vowelsArr) - 1
    for j in range(len(s)):
        if s[j] in vowels:
            reverseStr += vowelsArr[pointer]
            pointer -= 1
        else:
            reverseStr += s[j]
    return reverseStr

print(reverseVowelsOfAString("hello"))
print(reverseVowelsOfAString("leetcode"))
print(reverseVowelsOfAString("aA"))
     