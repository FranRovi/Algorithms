# Leet Code 3005. Count Elements with Maximum Frequency

def countElementsWithMaximumFrequency(nums):
    counter = 0
    hashElements = {}
    for i in range(len(nums)):
        if nums[i] not in hashElements:
            hashElements[nums[i]] = 1
        else:
            hashElements[nums[i]] += 1
    
    tupleElementsOrderedByFrequency = sorted(hashElements.items(), key= lambda x:x[1], reverse=True)
    sortedHashElementByFrequency = dict(tupleElementsOrderedByFrequency)
        
    maxFreqKey = (list(sortedHashElementByFrequency.keys())[0])
    print(sortedHashElementByFrequency, maxFreqKey)
    
    for value in sortedHashElementByFrequency.values():
        if value == sortedHashElementByFrequency[maxFreqKey]:
            counter += value
        else:
            break
    return counter   
    
    
    
print(countElementsWithMaximumFrequency([1,2,2,3,1,4]))
print(countElementsWithMaximumFrequency([1,2,3,4,5]))