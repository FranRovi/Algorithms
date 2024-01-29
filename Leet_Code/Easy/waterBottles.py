# Leet Code Algo 1518. Water Bottles

def waterBottles(numBottles, numExchange):
    drinkBottles = numBottles
    bottlesToExchange = int(numBottles / numExchange)
    bottlesEmpty = numBottles % numExchange
    drinkBottles += bottlesToExchange
    bottlesRem = bottlesToExchange + bottlesEmpty
    while bottlesRem >= numExchange:
        bottlesToExchange = int(bottlesRem / numExchange)
        bottlesEmpty = bottlesRem % numExchange
        drinkBottles += bottlesToExchange
        bottlesRem = bottlesToExchange + bottlesEmpty
    return drinkBottles
        
print(waterBottles(9, 3))    
print(waterBottles(15, 4))
        