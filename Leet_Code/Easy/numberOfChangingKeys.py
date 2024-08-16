# Leet Code Algo 3019. Number of Changing Keys

def countKeyChanges(s):
    counter = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i-1].lower():
            counter += 1
    return counter

print(countKeyChanges("aAbBcC"))
print(countKeyChanges("AaAaAaaA"))
