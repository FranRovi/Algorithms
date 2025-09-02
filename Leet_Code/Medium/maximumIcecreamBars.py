# Leet Code Algo 1833. Maximum Ice Cream Bars

def maxIceCream(costs, coins):
    counter = 0
    money_spended = 0
    sorted_costs = sorted(costs)
    if coins < sorted_costs[0]:
        return 0
    for i in range(len(sorted_costs)):
        if money_spended + sorted_costs[i] > coins:
            break
        else:
            money_spended += sorted_costs[i]
            counter += 1
    return counter

print(maxIceCream([1,3,2,4,1], 7))
print(maxIceCream([10,6,8,7,7,8], 5))
print(maxIceCream([1,6,3,1,2,5], 20))