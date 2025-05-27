# Leet Code Algo 1979. Find Greatest Common Divisor of Array

def findGDC(nums):
    max_num = 2
    min_num = 1000

    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    if min_num == max_num:
        return min_num
    max_div = 1

    # GDC
    while True:
        result = max_num % min_num
        if result == 0:
            return min_num
        max_num = min_num
        min_num = result 
    
    # BRUTE FORCE
    # for i in range(2, max_num+1):
    #     if min_num % i == 0 and max_num % i == 0:
    #         max_div = i
    # return max_div
    
print(findGDC([2,5,6,9,10]))
print(findGDC([7,5,6,8,3]))
print(findGDC([3,3]))
print(findGDC([6,7,9]))