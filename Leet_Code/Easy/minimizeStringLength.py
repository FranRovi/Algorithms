# Leet Code Algo 2716. Minimize String Length

def minimizeStringLength(s):
    hashChar = {}
    counter = 0
    for i in range(len(s)):
        if s[i] not in hashChar:
            hashChar[s[i]] = 1
        else:
            hashChar[s[i]] += 1
    for key, value in hashChar.items():
        counter += 1
    return counter
    
print(minimizeStringLength('aaabc'))
print(minimizeStringLength('cbbd'))  
print(minimizeStringLength('dddaaa'))      