# Hacker Rank Algo Pangrams

def pangrams(s):
    sLower = s.lower()
    hashLettersFreq = {}
    counter = 0
    for i in range(len(sLower)):
        if sLower[i].isalpha():
            if sLower[i] not in hashLettersFreq:
                hashLettersFreq[sLower[i]] = 1
                counter += 1
            else:
                hashLettersFreq[sLower[i]] += 1
    if counter < 26:
        return 'not pangram'
    return 'pangram'

print(pangrams('Te quick brown fox jumps over the lazy dog'))
print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))