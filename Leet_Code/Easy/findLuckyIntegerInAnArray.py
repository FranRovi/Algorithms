# Leet Code Algo 1394. Find Lucky Integer In An Array

def findLuckyIntegerInAnArray(arr):
    hashArr = {}
    for i in range(len(arr)):
        if arr[i] not in hashArr:
            hashArr[arr[i]] = 1
        else:
            hashArr[arr[i]] += 1
    
    sortedHashArrByKeyTup = sorted(hashArr.items(), reverse=True)
    sortedDictHashArr = dict(sortedHashArrByKeyTup)

    for key, value in sortedDictHashArr.items():
        if key == value:
            return key
    return -1

print(findLuckyIntegerInAnArray([2,2,3,4]))
print(findLuckyIntegerInAnArray([1,2,2,3,3,3]))
print(findLuckyIntegerInAnArray([2,2,2,3,3])) 
