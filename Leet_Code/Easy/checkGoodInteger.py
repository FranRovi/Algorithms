# Leet Code Algo 3959. Check Good Integer

def checkGoodInteger(n):
    digit_sum = 0
    square_sum = 0
    str_n = str(n)
    for c in str_n:
        temp = int(c) 
        digit_sum += temp
        square_sum += temp ** 2
    return True if square_sum - digit_sum >= 50 else False

print(checkGoodInteger(1000))
print(checkGoodInteger(19))
        