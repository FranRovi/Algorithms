# Leet Code Algo 2744. Maximum Numbers of String Pairs

def maximumNumbersOfStringPairs(words):
    counter = 0
    hashStrings = {}
    hashStrings[words[0]] = 1
    for i in range(1, len(words)):
        temp = words[i][1] + words[i][0]
        if words[i] and temp not in hashStrings:
            hashStrings[words[i]] = 1
        else:
            counter += 1
    return counter

print(maximumNumbersOfStringPairs(["cd","ac","dc","ca","zz"]))
print(maximumNumbersOfStringPairs(["ab","ba","cc"]))
print(maximumNumbersOfStringPairs(["aa","ab"]))

 