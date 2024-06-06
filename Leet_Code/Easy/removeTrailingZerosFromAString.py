# Leet Code Algo 2710. Remove Trailing Zeros From a String

def removeTrailingZeros(num):
    isConsecutiveZero = False
    counter = 0
    answer = ""
    for i in range(len(num)):
        if num[i] != "0":
            isConsecutiveZero = False
            counter = 0
        else:
            isConsecutiveZero = True
        if isConsecutiveZero and num[i] == "0":
            counter += 1
    for j in range(len(num) - counter):
        answer += num[j]
    return answer

print(removeTrailingZeros("51230100"))
print(removeTrailingZeros("123"))    
