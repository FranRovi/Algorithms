# Leet Code Algo 2315. Count Asteriks

def countAsteriks(s):
    counterAsteriks = 0
    verticalBars = 0
    for i in range(len(s)):
        if s[i] == '|':
            verticalBars += 1
        if verticalBars % 2 == 0 and s[i] == '*':
            counterAsteriks += 1
    return counterAsteriks

print(countAsteriks('l|*e*et|c**o|*de|'))
print(countAsteriks('iamprogrammer'))
print(countAsteriks('*||*|||||*|*|***||*||***|'))