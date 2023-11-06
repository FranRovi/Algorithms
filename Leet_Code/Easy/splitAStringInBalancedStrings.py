# Leet Code 1221. Split a String in Balanced Strings

def splitAStringInBalancedStrings(s):
    counter = 0
    rCounter = 0
    lCounter = 0
    for i in range(len(s)):
        # print(s[i])
        if s[i] == "R":
            rCounter +=1
        elif s[i] == "L":
            lCounter += 1
        if rCounter == lCounter:
            counter += 1
    return counter

print(splitAStringInBalancedStrings("RLRRLLRLRL"))
print(splitAStringInBalancedStrings("RLRRRLLRLL"))