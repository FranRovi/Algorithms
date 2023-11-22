# Leet Code Algo 2535. Difference Between Element Sum and Digit Sum of an Array

def differenceBetweenElementSumAndDigitSumOfAnArray(nums):
    elementSum = 0
    numsSum = 0
    
    for num in nums:
        elementSum += num
        
        if num > 9:
            tempNumStr = str(num)
            for i in range(len(tempNumStr)):
                numsSum += int(tempNumStr[i])
        else: 
            numsSum += num
    
    return abs(elementSum - numsSum)  

print(differenceBetweenElementSumAndDigitSumOfAnArray([1,15,6,3]))
print(differenceBetweenElementSumAndDigitSumOfAnArray([1,2,3,4]))