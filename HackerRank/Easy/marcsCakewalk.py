# Hacker Rank Algo Marc's Cake Walk

def marcsCakewalk(calorie):
    total = 0
    sortedCalories = sorted(calorie, reverse= True)
    for i in range(len(sortedCalories)):
        total += (2 ** i) * sortedCalories[i]
    return total

print(marcsCakewalk([7,4,9,6]))