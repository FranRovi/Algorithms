# Leet Code Algo 2697. Lexicographically Smallest Palindrome

def makeSmallestPalindrome(s):
    answerArr = [0] * len(s)
    leftIdx = 0
    rightIdx = len(s) -1
    while leftIdx < rightIdx:
        if s[leftIdx] < s[rightIdx]:
            answerArr[leftIdx] = s[leftIdx]
            answerArr[rightIdx] = s[leftIdx]
        else:
            answerArr[leftIdx] = s[rightIdx]
            answerArr[rightIdx] = s[rightIdx]
        leftIdx += 1
        rightIdx -= 1
    if len(s) % 2 != 0:
        answerArr[leftIdx] = s[leftIdx]
    smallestPalindrome = ''
    for char in answerArr:
        smallestPalindrome += char
    return smallestPalindrome

print(makeSmallestPalindrome("egcfe"))
print(makeSmallestPalindrome("abcd"))
print(makeSmallestPalindrome("seven"))