# Leet Code Algo 2864. Maximum Odd Binary Number

def maximumBinaryOddNumber(s):
    oneCounter = 0
    zeroCounter = 0
    answer = ""
    for i in range(len(s)):
        if int(s[i]) == 1:
            oneCounter += 1
    zeroCounter = len(s) - oneCounter
    for j in range(oneCounter - 1):
        answer += "1"
    for k in range(zeroCounter):
        answer += "0"
    answer += "1"
    return answer

print(maximumBinaryOddNumber("010"))
print(maximumBinaryOddNumber("0101"))