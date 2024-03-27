# Hacker Rank Algo Camel Case

def camelCase(s):
    counter = 1
    for i in range(len(s)):
        if s[i].isupper():
            counter += 1
    return counter

print(camelCase('saveChangesInTheEditor'))
print(camelCase('iAmAwesome'))