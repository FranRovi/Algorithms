# Leet Code 575. Distribute Candies

def distributeCandies(candies):
    hmCandies = {}
    totalCandies = 0
    difTypeCandies = 0
    for i in range(len(candies)):
        if (hmCandies.get(candies[i]) == None):
            hmCandies[candies[i]] = 1
        else:
            hmCandies[candies[i]] += 1
    
    for key, value in hmCandies.items():
        difTypeCandies += 1
        totalCandies += value
    if ((totalCandies / 2) > difTypeCandies):
        return int(difTypeCandies)
    else:
        return int(totalCandies / 2)
        

print(distributeCandies([1,1,2,2,3,3]))
print(distributeCandies([1,1,2,3]))
print(distributeCandies([6,6,6,6]))
