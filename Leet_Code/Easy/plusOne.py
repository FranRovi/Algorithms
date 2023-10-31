# Leet Code 66. Plus One

def plusOne(digits):
    if len(digits) == 1:
        if digits[0] >= 0 and digits[0] <= 8:
            return digits[0] + 1 
        elif digits[0] == 9:
            return [1, 0]
        else:
            return [1, 0]
    for i in range(len(digits)-1,-1,-1):
        if (digits[i] < 9):
            digits[i] += 1
            break
        else:
            digits[i] = 0
    if digits[0] == 0:
        digits.insert(0, 1)        
    return digits
        
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([1,3,9]))
print(plusOne([9,9,9]))



