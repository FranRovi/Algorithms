# Leet Code Algo 1056. Confusing Number

def confusingNumber(n):
    str_num = str(n)
    hash_nums = {}
    valid_digits = ["0","1","6","8","9"]
    valid_nums = ["101","619","906","916"]

    for i in range(len(str_num)):
        if str_num[i] not in hash_nums:
            hash_nums[str_num[i]] = 1
        else:
            hash_nums[str_num[i]] += 1
    if len(hash_nums) == 1 and n in [6,9]:
        return True
    elif str_num in valid_nums:
        return False
    elif len(hash_nums) > 1:
        for key, value in hash_nums.items():
            if key not in valid_digits:
                return False
        return True
    return False

print(confusingNumber(6))
print(confusingNumber(89))
print(confusingNumber(11))      