# Leet Code Algo 2610. Convert an Array Into a 2D Array with Conditions

def convertAnArrayIntoA2DArrayWithConditions(nums):
    answer = []
    frequencyNumDict = {}
    for i in range(len(nums)):
        if nums[i] not in frequencyNumDict:
            frequencyNumDict[nums[i]] = 1
        else:
            frequencyNumDict[nums[i]] += 1
    sortedDictByValueTup = sorted(frequencyNumDict.items(), key=lambda x:x[1], reverse=True)
    sortedDictByValueDic = dict(sortedDictByValueTup)
    mostFreqNum = next(iter(sortedDictByValueDic))
    freqNumRep = sortedDictByValueDic[mostFreqNum]
    for i in range(freqNumRep):
        answer.append([])
    for key, value in frequencyNumDict.items():        
        for j in range(value):
            answer[j].append(key)
        
    return answer

print(convertAnArrayIntoA2DArrayWithConditions([1,3,4,1,2,3,1]))
print(convertAnArrayIntoA2DArrayWithConditions([1,2,3,4]))
    