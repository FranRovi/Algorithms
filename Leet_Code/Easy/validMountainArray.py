# Leet Code Algo 941. Valid Mountain Array

def validMountainArray(arr):
    if len(arr) < 3:
        return False
    counter = 0
    highestNum = arr[0]
    highestNumIdx = 0
    isAscending = False
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            if arr[i - 1] == arr[i]:
                return False 
            else:
                counter += 1
        if arr[i] > highestNum:
            isAscending = True
            highestNum = arr[i]
            highestNumIdx = i                
        elif arr[i] == highestNum:
            return False
    if counter == 0 or not isAscending:
        return False
    if counter != 1:
        if len(arr) - 1 - highestNumIdx != counter:
            return False
    return True

print(validMountainArray([2,1]))
print(validMountainArray([3,5,5]))
print(validMountainArray([0,3,2,1]))
print(validMountainArray([2,0,2]))
print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))