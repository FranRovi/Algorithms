# Leet Code Algo 125. Valid Palindrome

def isPalindrome(s):
    cleanStr = ""
    for char in s:
        if char.isalnum():
            if char.isalpha():
                cleanStr += char.lower()
            else:
                cleanStr += char
    leftIdx = 0
    rightIdx = len(cleanStr) - 1
    while leftIdx <= rightIdx:
        if cleanStr[leftIdx] != cleanStr[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("0P"))