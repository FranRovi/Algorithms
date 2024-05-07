# Hacker Rank Algo Beautiful Binary String 

def beautifulBinaryString(b):
    bList = list(b)
    counter = 0
    if len(bList) < 3:
        return counter
       
    for i in range(len(bList) - 2):
        if (bList[i] == '0' and
            bList[i + 1] == '1' and
            bList[i + 2] == '0'):
                counter += 1
                bList[i + 2] = '1'
    return counter

print(beautifulBinaryString('0101010'))
print(beautifulBinaryString('01100'))
print(beautifulBinaryString('0100101010'))
        