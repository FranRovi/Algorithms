# Leet Code Algo 3908. Valid Digit Number

def validDigit(n, x):
    is_present = False
    str_num = str(n)
    for num in str_num:
        if num == str(x):
            is_present = True
            break
    if is_present and str_num[0] != str(x):
        return True
    return False

print(validDigit(101, 0))
print(validDigit(232, 2))
print(validDigit(5, 1))