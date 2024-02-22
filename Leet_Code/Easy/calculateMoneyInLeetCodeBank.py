# Leet Code Algo 1716. Caluclate Money in Leet Code Bank

def calculateMoney(n):
    totalMoney = 0
    currentWeek = 0
    days = 1
    moneyToAdd = days
    for i in range(1, n + 1):
        if i % 7 == 0:
            totalMoney += 6
            days = 1
            currentWeek += 1
            moneyToAdd = currentWeek
        totalMoney += moneyToAdd
        moneyToAdd += 1
    return totalMoney
print(calculateMoney(4))
print(calculateMoney(10))    
print(calculateMoney(20))
    