# Leet Code 1925. Count Square Sum Triplets.

def countTriplets(n):
    counter = 0
    for i in range(1, n - 1):
        if i ** 2 + i+1 ** 2 > n ** 2:
            break
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if i ** 2 + j ** 2 == k ** 2:
                    counter += 1
    return counter * 2

print(countTriplets(5))
print(countTriplets(10))