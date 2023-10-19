# Leet Code 1478. Sum of Unique Elements

def sumOfUniqueElements(nums):
    hashUniqueEle = {}
    
    for i in range(len(nums)):
        if nums[i] not in hashUniqueEle:
            hashUniqueEle[nums[i]] = 1
        else:
            hashUniqueEle[nums[i]] += 1
        
    totalSum = 0
    
    for key, val in hashUniqueEle.items():
        if val == 1:
                totalSum += key
    return totalSum

print(sumOfUniqueElements([1,2,3,2]))
print(sumOfUniqueElements([1,1,1,1,1]))
print(sumOfUniqueElements([1,2,3,4,5]))