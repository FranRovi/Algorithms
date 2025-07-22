# Leet Code Algo 3622. Check Divisibility by Digit Sum and Product

def checkDivisibility(n):
    num_list = list(map(int, str(n)))
    digit_sum = 0
    digit_prod = 1
    for i in range(len(num_list)):
        digit_sum += num_list[i]
        digit_prod *= num_list[i]
    if n % (digit_sum + digit_prod) == 0:
        return True
    return False

print(checkDivisibility(99))
print(checkDivisibility(23))