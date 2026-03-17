# Leet Code Algo 1309. Decrypt String from Alphabet to Integer Mapping.

def freqAlphabets(s):
    hashNumToChar = {
        1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l",
        13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w",
        24:"x", 25:"y", 26:"z"
    }
    answer = ""
    idx = len(s) - 1
    while idx >= 0:
        if s[idx] == "#":
            temp = int(s[idx-2] + s[idx-1]) 
            answer = hashNumToChar[temp] + answer
            idx -= 3  
        else:
            answer = hashNumToChar[int(s[idx])] + answer
            idx -= 1
    return answer

print(freqAlphabets("10#11#12"))
print(freqAlphabets("1326#"))
