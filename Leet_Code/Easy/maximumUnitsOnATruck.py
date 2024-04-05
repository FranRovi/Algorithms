# Leet Code Algo 1710. Maximum Units on a Truck 

def maximumUnitsOnTrack(boxTypes, truckSize):
    counter = 0
    totalItems = 0
    hashItemsQuantity = {}
    for i in range(len(boxTypes)):
        if boxTypes[i][1] not in hashItemsQuantity:
            hashItemsQuantity[boxTypes[i][1]] = boxTypes[i][0]
        else:
            hashItemsQuantity[boxTypes[i][1]] += boxTypes[i][0]
    sortedTupleQuantity = sorted(hashItemsQuantity.items(), reverse=True)
    sortedHashQuality = dict(sortedTupleQuantity)
    for key, value in sortedHashQuality.items():
            for j in range(1, value+1):
                if counter < truckSize:
                    totalItems += key
                    counter += 1
                else:
                    break
    return totalItems

print(maximumUnitsOnTrack([[1,3],[2,2],[3,1]], 4))
print(maximumUnitsOnTrack([[5,10],[2,5],[4,7],[3,9]], 10))
print(maximumUnitsOnTrack([[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]], 13))