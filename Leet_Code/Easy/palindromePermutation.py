# Leet Code Algo 266. Palindrome Permutation.

def canPermutePalindrome(s):
    hash_char = {}
    for char in s:
        if char not in hash_char:
            hash_char[char] = 1
        else:
            hash_char[char] += 1
    one_counter = 0
    even_counter = 0
    for key, value in hash_char.items():
        if value == 1:
            one_counter += 1
        if value % 2 == 0:
            even_counter += 1

    if len(hash_char) == 1:
        return True
    if len(hash_char) == even_counter:
        return True
    if len(hash_char) - 1 == even_counter:
        return True
    return False

print(canPermutePalindrome("code"))
print(canPermutePalindrome("aab"))
print(canPermutePalindrome("carerac"))
print(canPermutePalindrome("aa"))
print(canPermutePalindrome("aabb"))
print(canPermutePalindrome("aabbccc"))