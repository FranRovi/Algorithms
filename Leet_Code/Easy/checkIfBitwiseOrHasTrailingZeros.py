# Leet Code Algo 2980. Check if Bitwise OR Has Trailing Zeros

def hasTrailingZeros(nums):
    counter = 0
    for num in nums:
        if num % 2 == 0:
            counter += 1
        if counter >= 2:
            return True
    return False

print(hasTrailingZeros([1,2,3,4,5]))
print(hasTrailingZeros([2,4,8,16]))
print(hasTrailingZeros([1,3,5,7,9]))