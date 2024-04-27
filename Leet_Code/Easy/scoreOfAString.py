# Leet Code Algo 3110. Score of a String

def scoreOfAString(s):
    totalSum = 0
    for i in range(1, len(s)):
        totalSum += abs(ord(s[i-1]) - ord(s[i]))
    return totalSum

print(scoreOfAString("hello"))
print(scoreOfAString("zaz"))