# Leet Code Algo 3950. Exactly One Consecutive Set Bits Pair

def consecutiveBits(n):
    bin_n = bin(n)[2:]
    counter = 0

    for i in range(len(bin_n)-1):
        if bin_n[i] == "1" and bin_n[i] == bin_n[i+1]:
            counter += 1
        if counter == 2:
            return False
    if counter == 0:
        return False
    return True

print(consecutiveBits(6))
print(consecutiveBits(5))
print(consecutiveBits(12))
print(consecutiveBits(37))