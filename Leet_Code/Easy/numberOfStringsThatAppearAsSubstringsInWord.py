# Leet Code Algo 1967. Number of Strings That Appear as Substrings in Word

def numOfStrings(patterns, word):
    counter = 0
    for i in range(len(patterns)):
        if patterns[i] in word:
            counter += 1
    return counter

print(numOfStrings(["a", "abc", "bc", "d"], "abc"))
print(numOfStrings(["a", "b", "c"], "aaaaabbbbb"))
print(numOfStrings(["a", "a", "a"], "ab"))