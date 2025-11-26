# Leet Code Algo 3750. Minimum Number of Flips to Reverse Binary String

def intToBit(n):
    reversedBitArr = []
    while n >= 2:
        if n % 2 == 0:
            reversedBitArr.append(0)
        else:
            reversedBitArr.append(1)
        n = n // 2
    reversedBitArr.append(1)
    reversed_Bit = ""
    for char in reversedBitArr:
        reversed_Bit += str(char)
    return reversed_Bit
    
def minimumFlips(n: int) -> int:
    temp_bin = intToBit(n)

    bitNumStr = ""
    for i in range(len(temp_bin)-1,-1,-1):
        bitNumStr += str(temp_bin[i])

    counter = 0
    for j in range(len(temp_bin)):
        if temp_bin[j] != bitNumStr[j]:
            counter += 1 
    return counter

print(minimumFlips(7))
print(minimumFlips(10))
