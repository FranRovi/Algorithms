# Leet Code 13. Roman to Integer

def romanToInteger(romanNum: str) -> int:
    romanDict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    totalInt = 0
    prevNum = 0
    
    for i in range(len(romanNum)):
        if (prevNum < romanDict.get(romanNum[i])):
            totalInt += romanDict.get(romanNum[i]) - 2 * prevNum
        else:  
            totalInt += romanDict.get(romanNum[i])
        prevNum = romanDict.get(romanNum[i])
    
    return totalInt

print(romanToInteger("III"))
print(romanToInteger("XII"))
print(romanToInteger("XXVII"))
print(romanToInteger("MCMXCIV"))
   