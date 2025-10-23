# Leet Code Algo 693. Binary Number with Alternating Bits

def hasAlternatingBits(n):
    binary_n = bin(n)
    binary_n_str = binary_n[2:]
    for i in range(len(binary_n_str)-1):
        if binary_n_str[i] == binary_n_str[i+1]:
            return False
    return True

print(hasAlternatingBits(5))
print(hasAlternatingBits(7))
print(hasAlternatingBits(11))