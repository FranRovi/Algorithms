# Leet Code Algo 2553. Separate Digits in an Array

def separateTheDigitsInAnArray(nums):
    newArr = []
    for i in range(len(nums)):
        if len(str(nums[i])) > 1:
            strNum = str(nums[i])
            for j in range(len(strNum)):
                newArr.append(int(strNum[j]))
        else:
            newArr.append(nums[i])
    return newArr

print(separateTheDigitsInAnArray([14,25,9,83,77]))
print(separateTheDigitsInAnArray([7,1,3,9,77]))