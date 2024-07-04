# Leet Code Algo 2073. Time Needed to Buy Tickets

def timeRequiredToBuy(tickets, k):
    counter = 0
    while tickets[k] != 0:
        for i in range(len(tickets)):
            if tickets[k] == 0:
                return counter
            if tickets[i] > 0:
                counter += 1
                tickets[i] -= 1
    return counter
            
print(timeRequiredToBuy([2,3,2], 2))
print(timeRequiredToBuy([5,1,1,1], 0))
            