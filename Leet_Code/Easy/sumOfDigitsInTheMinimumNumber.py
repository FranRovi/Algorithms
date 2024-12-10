# Leet Code Algo 1085. Sum of Digits in the Minimum Number

def sumOfDigits(nums):
    minNum = nums[0]
    for num in nums:
        if num < minNum:
            minNum = num
    strNum = str(minNum)
    totalSum = 0
    for char in strNum:
        totalSum += int(char)
    return 1 if totalSum % 2 == 0 else 0

print(sumOfDigits([34,23,1,24,75,33,54,8]))
print(sumOfDigits([99,77,33,66,55]))