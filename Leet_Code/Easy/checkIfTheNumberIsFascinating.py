# Leet Code Algo 2729. Check if The Number if Fascinating

def isFascinating(n):
    nStr = str(n) + str(n * 2) + str(n * 3)
    hashNums = {}
    for i in range(len(nStr)):
        if nStr[i] not in hashNums:
            hashNums[nStr[i]] = 1
        else:
            hashNums[nStr[i]] += 1
    for key, value in hashNums.items():
        if key == '0' or value != 1:
            return False
    return True

print(isFascinating(192))
print(isFascinating(100))
print(isFascinating(267))
