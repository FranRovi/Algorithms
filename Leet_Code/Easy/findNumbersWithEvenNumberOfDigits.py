# Leet Code Algo 1295. Find Numbers With Even Number Of Digits

def findNumbers(nums):
    counter = 0
    for num in nums:
        temp = len(str(num))
        if temp % 2 == 0:
            counter += 1
    return counter

print(findNumbers([12, 345, 2, 6, 7896]))
print(findNumbers([555, 901, 482, 1771]))