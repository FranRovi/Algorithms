# Leet Code Algo 2190. Most Frequent Number Following Key in an Array

def mostFrequent(nums, key):
    freqValAfterKey = {}
    for i in range(len(nums)-1):
        if nums[i] == key:
            if nums[i+1] not in freqValAfterKey:
                freqValAfterKey[nums[i+1]] = 1
            else:
                freqValAfterKey[nums[i+1]] += 1
    #print(freqValAfterKey)
    sortedDictByValueTup = sorted(freqValAfterKey.items(), key=lambda item: item[1], reverse=True)
    sortedDictByKey = dict(sortedDictByValueTup)
    #print(sortedDictByKey)
    for key, value in sortedDictByKey.items():
        return key
    
print(mostFrequent([11,22,11,33,11,33], 11))

