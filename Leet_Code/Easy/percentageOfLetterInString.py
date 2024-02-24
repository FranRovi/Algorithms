# Leet Code Algo 2278. Percentage of Letter in a String
import math

def percentageOfLetterInAString(s, letter):
    stringLen = len(s)
    counter = 0
    for i in range(len(s)):
        if s[i] == letter:
            counter += 1
    return math.trunc((counter / stringLen) * 100)

print(percentageOfLetterInAString('foobar', 'o'))
print(percentageOfLetterInAString('jjjj', 'k'))

        