# Leet Code Algo 1207. Unique Number of Occurrences

def uniqueNumberOfOccurrences(arr):
    occurrencesHash = {}
    numOfOccurrences = []
    for i in range(len(arr)):
        if arr[i] not in occurrencesHash:
            occurrencesHash[arr[i]] = 1
        else:
            occurrencesHash[arr[i]] += 1
    for k,v in occurrencesHash.items():
        numOfOccurrences.append(v)
    setOccurrences = set(numOfOccurrences)
    if len(numOfOccurrences) == len(setOccurrences):
        return True
    else:
        return False
    
print(uniqueNumberOfOccurrences([1,2,2,1,1,3]))
print(uniqueNumberOfOccurrences([1,2]))
print(uniqueNumberOfOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))