# Leet Code Algo 342. Power of Four

def isPowerOfFour(n):
    idx = 0
    while 2 ** idx <= n:
        if 2 ** idx == n:
            return True
        idx += 1
    return False

print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
print(isPowerOfFour(64))