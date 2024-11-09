# Leet Code Algo 3210. Find the Encrypted String

def getEncryptedString(s, k):
    answer = ""
    for i in range(len(s)):
        answer += s[(i+k)%len(s)]
    return answer

print(getEncryptedString("dart", 3))
print(getEncryptedString("aaa", 1))