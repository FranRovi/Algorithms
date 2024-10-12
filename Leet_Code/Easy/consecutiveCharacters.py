# Leet Code Algo 1446. Consecutive Characters

def maxPower(s):
    if len(s) == 1:
        return 1
    maxPowerChar = 0
    temp = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            temp += 1
        else:
            if temp > maxPowerChar:
                maxPowerChar = temp
            temp = 0
    if temp > maxPowerChar:
        maxPowerChar = temp
    return maxPowerChar + 1

print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))