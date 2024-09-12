# Leet Code Algo 2103. Rings and Rods

def countPoints(rings):
    hashRods = {}
    counter = 0
    for i in range(0,len(rings), 2):
        if rings[i+1] not in hashRods:
            hashRods[rings[i+1]] = set(rings[i])
        else:
            hashRods[rings[i+1]].add(rings[i])
    for item in hashRods.items():
        print(item[1])
        if len(item[1]) == 3:
            counter += 1
    return counter

print(countPoints("B0B6G0R6R0R6G9"))
print(countPoints("B0R0G0R9R0B0G0"))
print(countPoints("G4"))