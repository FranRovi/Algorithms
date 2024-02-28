def sockMatches(n , arr):
    hashSocks = {}
    pairCounter = 0
    
    for i in range(n):
        if arr[i] not in hashSocks:
            hashSocks[arr[i]] = 1
        else:
            hashSocks[arr[i]] += 1
    # print(hashSocks)
    for key, val in hashSocks.items():
        # print(val // 2)
        pairCounter += val // 2
    # print(pairCounter)
    return pairCounter
print(sockMatches(7, [1,2,1,2,1,3,2]))
print(sockMatches(9, [10,20,20,10,10,30,50,10,20]))
