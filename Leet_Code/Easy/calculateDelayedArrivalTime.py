# Leet Code Algo 2651. Calculate Delayed Arrival Time 

def calculateDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24

print(calculateDelayedArrivalTime(15, 5))
print(calculateDelayedArrivalTime(13, 11))
