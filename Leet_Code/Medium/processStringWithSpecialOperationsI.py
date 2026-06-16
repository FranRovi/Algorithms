# Leet Code Algo 3612. Process String with Special Operations I

def reverseString(s):
    temp = ""
    for i in range(len(s)-1,-1,-1):
        temp += s[i]
    return temp
    
def processStr(s):
    answer = ""
    for c in s:
        if c == "%":
            answer = reverseString(answer)
        elif c == "*":
            answer = answer[:len(answer)-1]
        elif c == "#":
            answer = answer + answer
        else:   
            answer += c
    return answer

print(processStr("a#b%*"))
print(processStr("z*#"))
print(processStr("lby#m"))
            
            