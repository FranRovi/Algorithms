# Leet Code Algo 2148

def countElements(nums):
    counter = 0
    isSmaller = False
    isGreater = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                isGreater = True
            if nums[i] < nums[j]:
                isSmaller = True
        if isSmaller and isGreater:
            counter +=1
        isSmaller = False
        isGreater = False
    return counter
    
print(countElements([11,7,2,15]))
print(countElements([-3,3,3,90]))
