# Leet Code Algo 1271. Hexspeak

def toHeaxspeak(num):
    n = int(num)
    if n == 0:
        return "0"
    if n == 1: 
        return "I"
    if n < 10 and n > 2:
        return "ERROR"
    reversedBit = []
    bitNumStr = ""
    hash_nums_letters = {"0":"O","1":"I","10":"A","11":"B",
        "12":"C","13":"D","14":"E","15":"F","16":"G"}
    while n >= 16:
        temp = str(n % 16)
        if str(n % 16) in hash_nums_letters:
            reversedBit.append(hash_nums_letters[temp])
        else:
            reversedBit.append(str(temp))
        n = n // 16
    if str(n % 16) in hash_nums_letters:
        reversedBit.append(hash_nums_letters[str(n % 16)])
    else:
        reversedBit.append(str(n))
    valid_letters = {"A","B","C","D","E","F","G","I","O"}
    for i in range(len(reversedBit)-1,-1,-1):
        bitNumStr += str(reversedBit[i])
        if reversedBit[i] not in valid_letters:
            return "ERROR"
    return bitNumStr


print(toHeaxspeak(257))
print(toHeaxspeak(3))
print(toHeaxspeak(747823223228))
print(toHeaxspeak(619879596177))