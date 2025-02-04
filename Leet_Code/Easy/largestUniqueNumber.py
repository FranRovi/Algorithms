# Leet Code Algo 1133. Largest Unique Number

def largestUniqueNumber(nums):
    hashNums = {}
    for num in nums:
        if num not in hashNums:
            hashNums[num] = 1
        else:
            hashNums[num] += 1
    hashNumsTupleKeysSorted = sorted(hashNums.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    hashNumsDictKeysSorted = dict(hashNumsTupleKeysSorted)
    if len(hashNumsDictKeysSorted) == 0:
        return -1
    else: 
        for key, value in hashNumsDictKeysSorted.items():
            if value == 1:
                return key
        return -1

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))