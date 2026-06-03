# Leet Code Algo 3918. Sum of Primes Between Number and Its Reverse.

def isNumberPrime(n):
        square_root = int(n ** 0.5)
        for i in range(3, square_root+1, 2):
            if n % i == 0:
                return 0
        return 1
        

def sumOfPrimesInRange(n):
    if n == 1:
        return 0
    str_num = str(n)
    reverse_num_str = ""
    for i in range(len(str_num)-1,-1,-1):
        reverse_num_str += str_num[i]
    reverse_num_int = int(reverse_num_str)
    total_sum = 0
    start = 0
    end = 0
    if n >= reverse_num_int:
        end = n
        start = reverse_num_int
    else:
        start = n
        end = reverse_num_int
    if start <= 2:
        total_sum += 2
        start = 3
    if start % 2 == 0:
        start += 1
    for j in range(start, end+1,2):
        result = isNumberPrime(j)
        if result == 1:
            total_sum += j
    return total_sum

print(sumOfPrimesInRange(13))
print(sumOfPrimesInRange(10))
print(sumOfPrimesInRange(8))
print(sumOfPrimesInRange(102))
print(sumOfPrimesInRange(75))