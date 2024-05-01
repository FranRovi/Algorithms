# Hacker Rank Algo Funny String 

def funnyString(s):
    sOrd = []
    sReverseOrd = []
    
    for i in range(len(s)):
        sOrd.append(ord(s[i]))
    for j in range(len(s) -1, -1, -1):
        sReverseOrd.append(ord(s[j]))
    for k in range(1, len(s)):
        if (abs(sOrd[k -1] - sOrd[k]) !=
            abs(sReverseOrd[k -1] - sReverseOrd[k])):
            return "Not Funny"
    return "Funny"
    
print(funnyString('lmnop'))
print(funnyString('acxz'))
print(funnyString('bcxz'))