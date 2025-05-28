# Leet Code Algo 3074. Apple Redistribution into Boxes

def minimumBoxes(apple, capacity):
    count_apples = 0
    for a in apple:
        count_apples += a
    
    count_capacity = 0
    for c in capacity:
        count_capacity += c

    if count_apples == count_capacity:
        return len(capacity)
    
    sorted_capacity = sorted(capacity, reverse=True)
    counter = 0
    idx = 0
    while count_apples > 0:
        count_apples -= sorted_capacity[idx]
        counter +=1
        idx += 1
    return counter