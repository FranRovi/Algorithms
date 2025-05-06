# Leet Code Algo 3461. Check If Digits Are Equal in String After Operations I

def hasSameDigits(s):
    temp_str = s
    new_num_str = ""
    while (len(temp_str)) != 2:
        for i in range(1, len(temp_str)):
            new_num_str += str((int(temp_str[i-1]) + int(temp_str[i])) % 10)
        temp_str = new_num_str
        new_num_str = ""
    return True if temp_str[0] == temp_str[1] else False
    
print(hasSameDigits("3902"))
print(hasSameDigits("34789"))