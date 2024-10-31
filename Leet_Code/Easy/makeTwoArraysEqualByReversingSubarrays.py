# Leet Code Algo 1460. Make Two Arrays Equal By Reversing Subarrays

def canBeEqual(target, arr):
    hashTarget = {}
    for num in target:
        if num not in hashTarget:
            hashTarget[num] = 1
        else:
            hashTarget[num] += 1
    
    hashArr = {}
    for num in arr:
        if num not in hashArr:
            hashArr[num] = 1
        else:
            hashArr[num] += 1

    for key, value in hashTarget.items():
        if key not in hashArr or value != hashArr[key]:
            return False
    return True

print(canBeEqual([1,2,3,4],[2,4,1,3]))
print(canBeEqual([7],[7]))
print(canBeEqual([3,7,9],[3,7,11]))