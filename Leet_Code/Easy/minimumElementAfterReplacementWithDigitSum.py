# Leet Code Algo 3300. Minimum Element After Replacement With Digit Sum

def minElement(nums):
    smallest = 10000
    for num in nums:
        strNum = str(num)
        totalSum = 0
        for i in range(len(strNum)):
            totalSum += int(strNum[i])
        if totalSum < smallest:
            smallest = totalSum
    return smallest

print(minElement([10,12,13,14]))
print(minElement([1,2,3,4]))
print(minElement([999,19,199]))