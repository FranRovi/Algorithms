# Leet Code 1431. Kids With the Greatest Number of Candies

def kidsWIthTheGreatestNumberOfCandies(candies, extraCandies):
    maxNumOfCandies = 0
    boolArr = []
    for i in range(len(candies)):
        if candies[i] > maxNumOfCandies:
            maxNumOfCandies = candies[i]
        
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxNumOfCandies:
            boolArr.append(True)
        else:
            boolArr.append(False)
    return boolArr

print(kidsWIthTheGreatestNumberOfCandies([2,3,5,1,3], 3))
print(kidsWIthTheGreatestNumberOfCandies([4,2,1,1,2], 1))
print(kidsWIthTheGreatestNumberOfCandies([12,1,12], 10))
        