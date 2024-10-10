# Leet Code Algo 2455. Average Value of Even Numbers That Are Divisible by Three

def averageValue(nums):
    totalElements = 0
    totalSum = 0
    for num in nums:
        if num % 3 == 0 and num % 2 == 0:
            totalSum += num
            totalElements += 1
    if totalElements == 0:
        return 0
    else:
        return int(totalSum / totalElements)
    
print(averageValue([1,3,6,10,12,15]))
print(averageValue([1,2,4,7,10]))