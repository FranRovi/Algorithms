# Leet Code Algo 231. Power of Two

def isPowerOfTwo(n):
    idx = 0
    while 2 ** idx <= n:
        if 2 ** idx == n:
            return True
        idx += 1
    return False

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
print(isPowerOfTwo(8))