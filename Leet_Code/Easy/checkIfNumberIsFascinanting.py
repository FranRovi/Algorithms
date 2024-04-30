# Leet Code Algo 2729. Check If Number Is Fascinating

def isFascinating(n):
    nStr = str(n) + str(n * 2) + str(n * 3)
    hashNums = {}
    for i in range(len(nStr)):
        if nStr[i] not in hashNums:
            hashNums[nStr[i]] = 1
        else:
            hashNums[nStr[i]] += 1
    sortedHashByVals = sorted(hashNums.items(), key=lambda x:x[1], reverse=True)
    sortedValueHash = dict(sortedHashByVals)
    if (list(sortedValueHash.values())[1] and
        len(sortedValueHash.keys()) == 9):
        return True
    return False
    
print(isFascinating(192))
print(isFascinating(100))
    