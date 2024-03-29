# Hacker Rank Algo Minimum Distances 

def minimumDistances(a):
    elementsHash = {}
    for i in range(len(a)):
        if a[i] not in elementsHash:
            elementsHash[a[i]] = [i]
        else:
            elementsHash[a[i]].append(i)
    sortedElementHashByValue = sorted(elementsHash.items(), key= lambda x:x[1])
    sortedDictElementHash = dict(sortedElementHashByValue)
    minDistance = 100000
    for key, value in sortedDictElementHash.items():
        if len(value) >= 2:
            if abs(value[1] - value[0]) < minDistance:
                minDistance = abs(value[1] - value[0])     
    if minDistance == 100000:
        return -1
    else:
        return  minDistance
            
print(minimumDistances([3,2,1,2,3]))
print(minimumDistances([7,1,3,4,1,7]))
print(minimumDistances([1,2,3,4,10]))
