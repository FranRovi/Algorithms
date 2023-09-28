def mayorityElement(nums):
    occurrences = {}
    for i in range(len(nums)):
        if (occurrences.get(nums[i]) == None):
            occurrences[nums[i]] = 1
        else:
            occurrences[nums[i]]  += 1
    sortedTupleOccurrences = sorted(occurrences.items(), key= lambda x:x[1], reverse=True)
    sortedHashByOccurrences = dict(sortedTupleOccurrences)
    print(sortedHashByOccurrences)
    answer = dict(list(sortedHashByOccurrences.items())[0:1])
    key, val = next(iter(answer.items()))
    print(key)
    #print(val)

mayorityElement([3,2,3])
mayorityElement([2,2,1,1,1,2,2])
mayorityElement([1,2,3,4,4,5,6,6,6])