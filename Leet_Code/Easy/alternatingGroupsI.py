# Leet Code Algo 3206. Alternating Groups

def numberOfAlternatingGroups(colors):
    counter = 0
    for i in range(2,len(colors)):
            if (colors[i] == colors[(i - 2)]  and
            (colors[(i - 1)] != colors[i] or colors[(i - 1)] != colors[(i - 2)])):
                counter += 1
    if (colors[-1] == colors[1]  and
    (colors[0] != colors[1] or colors[0] != colors[-1])):
        counter += 1
    if (colors[-2] == colors[0]  and
    (colors[-1] != colors[0] or colors[0] != colors[-1])):
        counter += 1
    return counter

print(numberOfAlternatingGroups([1,1,1]))
print(numberOfAlternatingGroups([0,1,0,0,1]))
print(numberOfAlternatingGroups([0,0,1]))
print(numberOfAlternatingGroups([0,1,1]))