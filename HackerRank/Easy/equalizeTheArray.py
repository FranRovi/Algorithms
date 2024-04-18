# Hacker Rank Algo Equalize The Array

def equalizeTheArray(arr):
    hashArr = {}
    for i in range(len(arr)):
        if arr[i] not in hashArr:
            hashArr[arr[i]] = 1
        else:
            hashArr[arr[i]] += 1     
    sortedHashArrByValue = sorted(hashArr.items(), key= lambda x:x[1], reverse=True)
    sortedDictHashArr = dict(sortedHashArrByValue)
    return (len(arr) - list(sortedDictHashArr.items())[0][1])
    
print(equalizeTheArray([1,2,2,3]))
print(equalizeTheArray([3,3,2,1,3]))