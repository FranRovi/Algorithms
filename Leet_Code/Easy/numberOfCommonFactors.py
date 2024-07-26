# Leet Code Algo 2427. Number of Common Factors

def commonFactors(a,b):
    counter = 0
    if a < b:
        smaller = a
        greater = b
    else:
        smaller = b
        greater = a
    # print(smaller, greater)
    for i in range(1, smaller+1):
        if smaller % i == 0:
            if greater % i == 0:
                counter += 1
                print(i)
    return counter 

print(commonFactors(12, 6))
print(commonFactors(25, 30))
print(commonFactors(761, 253))