# Leet Code Algo 2243. Calculate Digit Sum of a String

def digitSum(s, k):
    new_num = ""
    total_sum = 0
    while len(s) > k:
        for i in range(len(s)):
            if i % k == 0:
                new_num += str(total_sum)
                total_sum = int(s[i])
            else:
                total_sum += int(s[i])
        new_num += str(total_sum)
        s = new_num[1:]
        new_num = ""
        total_sum = 0 
    return s

print(digitSum("11111222223",3 ))
print(digitSum("00000000", 3))