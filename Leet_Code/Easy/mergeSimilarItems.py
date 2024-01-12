# Leet Code Algo 2363. Merge Similar Items

def mergeSimilarItems(items1, items2):
    ret = []
    valueHash = {}
    for i in range(len(items1)):
        if items1[i][0] not in valueHash:
            valueHash[items1[i][0]] = items1[i][1]
        else:
            valueHash[items1[i][0]] += items1[i][1]
    for j in range(len(items2)):
        if items2[j][0] not in valueHash:
            valueHash[items2[j][0]] = items2[j][1]
        else:
            valueHash[items2[j][0]] += items2[j][1]
    sortedValueHash = sorted(valueHash.items())
    sortedValueHash = dict(sortedValueHash)
    for key, value in sortedValueHash.items():
        ret.append([key,value])
    return ret

mergeSimilarItems([[1,1], [4,5], [3,8]],[[3,1], [1,5]])
    