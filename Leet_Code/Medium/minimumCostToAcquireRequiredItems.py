# Leet Code 3789. Minimum Cost to Acquire Required Items.

def minimumCost(cost1, cost2, costBoth, need1, need2):
    total_sum = 0
    min_val = need1 if need1 <= need2 else need2
    max_val = need1 if need1 > need2 else need2
    if cost1 + cost2 > costBoth:
        total_sum = min_val * costBoth
        if min_val == max_val:
            return total_sum
        elif max_val == need2:
            if cost2 > costBoth: 
                total_sum += abs(need1 - need2) * costBoth
            else:
                total_sum += abs(need1 - need2) * cost2
        else:
            if cost1 > costBoth: 
                total_sum += abs(need1 - need2) * costBoth
            else:
                total_sum += abs(need1 - need2) * cost1
    else:
        total_sum = min_val * cost1 + min_val * cost2
        if min_val == max_val:
            return total_sum
        elif max_val == need2:
            if cost2 > costBoth: 
                total_sum += abs(need1 - need2) * costBoth
            else:
                total_sum += abs(need1 - need2) * cost2
        else:
            if cost1 > costBoth: 
                total_sum += abs(need1 - need2) * costBoth
            else:
                total_sum += abs(need1 - need2) * cost1
    return total_sum

print(minimumCost(3,2,1,3,2))
print(minimumCost(5,4,15,2,3))
print(minimumCost(5,4,15,0,0))
print(minimumCost(50,55,72,5,3))