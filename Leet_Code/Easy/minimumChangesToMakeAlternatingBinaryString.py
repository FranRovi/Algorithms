# Leet Code Algo 1758. Minimum Changes To Make Alternating Binary String

def minOperations(s):
    count_zero = 0
    count_one = 0

    arr_s = list(s)

    for i in range(len(arr_s)):
        if i % 2 == 0:
            if s[i] != "0":
                count_zero += 1
        else:
            if s[i] != "1":
                count_zero += 1
    
    for j in range(len(arr_s)):
        if j % 2 == 0:
            if s[j] != "1":
                count_one += 1
        else:
            if s[j] != "0":
                count_one += 1
                
    return count_zero if count_zero < count_one else count_one

print(minOperations("0100"))
print(minOperations("10"))
print(minOperations("1111"))