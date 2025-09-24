# Leet Code Algo 1346. Check If N and Its Double Exist

def checkIfExists(arr):
    hash_nums = {}
    for n in arr:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
    if 0 in hash_nums and hash_nums[0] >= 2:
        return True     
    for i in range(len(hash_nums)):
        if arr[i] == 0:
            continue
        elif arr[i] * 2 in hash_nums:
            return True
    return False
    
print(checkIfExists([10,2,5,3]))
print(checkIfExists([3,1,7,11]))
print(checkIfExists([2,3,3,0,0]))
print(checkIfExists([0,-2,2]))


