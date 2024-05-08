# Hacker Rank Algo Game of Thrones

def gameOfThronesI(s):
    oddCounter = 0
    hashString = {}
    for i in range(len(s)):
        if s[i] not in hashString:
            hashString[s[i]] = 1
        else:
            hashString[s[i]] += 1
    listChar =  list(hashString.values())
    for j in range(len(listChar)):
        if listChar[j] % 2 != 0:
            oddCounter += 1
    if oddCounter > 1:
        return "NO"
    return "YES"

print(gameOfThronesI("aaabbbb"))
print(gameOfThronesI("aabbccdd"))
print(gameOfThronesI("cdefghmnopqrstuvw"))
print(gameOfThronesI("cdcdcdcdeeeef"))
    