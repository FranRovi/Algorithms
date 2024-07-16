# Leet Code Algo 326. Power of Three

def isPowerOfThree(n):
    idx = 0
    if n < 0:
        while 3 ** idx <= n:
            if 3 ** idx == n:
                return True
            idx -= 1
        return False
    else:
        while 3 ** idx <= n:
            if 3 ** idx == n:
                return True
            idx += 1
        return False

print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(-1))