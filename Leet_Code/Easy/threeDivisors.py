# Leet Code Algo 1952. Three Divisors.

def isThree(n):
    counter = 2
    for i in range(2, n):
        if n % i == 0:
            counter += 1
            if counter > 3:
                return False
    if counter == 3:
        return True
    return False

print(isThree(2))
print(isThree(4))
print(isThree(12))