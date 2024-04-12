# Hacker Rank Algo Mars Exploration

def marsExploration(s):
    counter = 0
    for i in range(0,(len(s) - 2), 3):
        if s[i] != 'S':
            counter += 1
        if s[i + 1] != 'O':
            counter += 1
        if s[i + 2] != 'S':
            counter += 1
    return counter

print(marsExploration('SOSTOT'))
print(marsExploration('SOSSOT'))
print(marsExploration('SOSSPSSQSSOR'))
print(marsExploration('SOSSOSSOS'))
