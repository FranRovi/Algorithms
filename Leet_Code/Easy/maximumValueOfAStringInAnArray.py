# Leet Code Algo 2496. Maximum Value of a String in an Array.

def maximumValue(strs):
    maxVal = 0
    for i in range(len(strs)):
        if strs[i].isdigit():
            if int(strs[i]) > maxVal:
                maxVal = int(strs[i])
        else:
            if len(strs[i]) > maxVal:
                maxVal = len(strs[i])
    return maxVal

print(maximumValue(["alic3","bob","3","4","00000"]))
print(maximumValue(["1","01","001","0001"]))