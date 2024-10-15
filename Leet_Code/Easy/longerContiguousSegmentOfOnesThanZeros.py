# Leet Code Algo 1869. Longer Contiguous Segments of Ones than Zeros

def checkZerosOnes(s):
    if len(s) == 1:
            return True if s[0] == "1" else False
    maxCounterOfZeros = 0
    maxCounterOfOnes = 0
    temp = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            temp += 1
        else:
            if s[i-1] == "0" and temp > maxCounterOfZeros:
                    maxCounterOfZeros = temp
            if s[i-1] == "1" and temp > maxCounterOfOnes:    
                    maxCounterOfOnes = temp
            temp = 0
    if s[i] == "0" and temp > maxCounterOfZeros:
        maxCounterOfZeros = temp
    if s[i] == "1" and temp > maxCounterOfOnes:
        maxCounterOfOnes = temp
    if maxCounterOfOnes > maxCounterOfZeros:
        return True
    return False

print(checkZerosOnes("1101"))
print(checkZerosOnes("111000"))
print(checkZerosOnes("0000111"))
print(checkZerosOnes("110100010"))


        