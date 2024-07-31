# Leet Code Algo 3184. Count Pairs That Form a Complete Day

def countCompleteDayPairs(hours):
    counter = 0
    for i in range(len(hours) -1):
        for j in range(i+1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                counter += 1
    return counter
print(countCompleteDayPairs([12,12,30,24,24]))
print(countCompleteDayPairs([72,48,24,3]))