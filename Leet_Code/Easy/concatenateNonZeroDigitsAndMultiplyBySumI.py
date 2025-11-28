# Leet Code Algo 3754. Concatenate Non-Zero Digits and Multiply by Sum I

def sumAndMultiply(n):
    if n == 0:
        return 0
    str_n = str(n)
    non_zero_d_str = ""
    total_sum = 0
    for ele in str_n:
        if ele != "0":
            non_zero_d_str += ele
            total_sum += int(ele)
    return int(non_zero_d_str) * total_sum

print(sumAndMultiply(10203004))
print(sumAndMultiply(1000))
print(sumAndMultiply(0))
