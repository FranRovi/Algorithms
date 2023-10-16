# Leet Code 771. Jewels and Stones

def jewelsAndStones(jewels, stones):
    jewelsDict = {}
    counter = 0
    for i in range(len(jewels)):
        if jewels[i] not in jewelsDict:
            jewelsDict[jewels[i]] = 0
    for j in range(len(stones)):
        if stones[j] in jewelsDict:
            counter += 1 
    return counter

print(jewelsAndStones("aA", "aAAbbbb"))
print(jewelsAndStones("z", "ZZ"))