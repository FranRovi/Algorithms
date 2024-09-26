# Hacker Rank Algo. Alternating Characters

def alternatingCharacters(s):
    counter = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
    return counter

print(alternatingCharacters("AAAA"))
print(alternatingCharacters("BBBBB"))
print(alternatingCharacters("ABABABAB"))
print(alternatingCharacters("BABABA"))
print(alternatingCharacters("AAABBB"))