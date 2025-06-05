# Leet Code Algo 2144. Minimum Cost of Buying Candies With Discount

def minimum_cost(cost):
    if len(cost) <= 2:
        return sum(cost)
    sorted_cost = sorted(cost, reverse= True)
    
    counter = 1
    total_sum = 0
    
    for c in sorted_cost:
        if counter % 3 != 0:
            total_sum += c
        counter += 1
    return total_sum

print(minimum_cost([1,2,3]))
print(minimum_cost([6,5,7,9,2,2]))
print(minimum_cost([5,5]))

        