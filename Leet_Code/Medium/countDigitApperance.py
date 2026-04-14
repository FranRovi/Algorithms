# Leet Code Algo 3895. Count Digit Appearances.

def countDigitOccurrences(nums, digit):
    counter = 0
    str_digit = str(digit)
    for i in range(len(nums)):
        temp = str(nums[i])
        for j in range(len(temp)):
            if temp[j] == str_digit:
                counter += 1
    return counter

print(countDigitOccurrences([12,54,32,22], 2))
print(countDigitOccurrences([1,34,7], 9))
    