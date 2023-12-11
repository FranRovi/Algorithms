# Leet Code Algo 2413. Smallest Even Multiple

def smallestEvenMultiple(n):
    idx = 1
    while True:
        if idx % 2 == 0 and idx % n == 0:
            return idx
        else:
            idx += 1

print(smallestEvenMultiple(5))
print(smallestEvenMultiple(6))