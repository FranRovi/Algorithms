# Leet Code Algo 1903. Largest Odd Number In String

def largestOddNumber(nums):
    tempIdxOdd = -1
    for i in range(len(nums)):
        if int(nums[i]) % 2 != 0:
            tempIdxOdd = i

    if tempIdxOdd == len(nums) -1:
        return nums
    elif tempIdxOdd == -1:
        return ""
    else:
        return nums[:tempIdxOdd+1]
    
print(largestOddNumber("52"))
print(largestOddNumber("4206"))
print(largestOddNumber("35427"))