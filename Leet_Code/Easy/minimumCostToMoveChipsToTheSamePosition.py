# Leet Code Algo 1217. Minimum Cost to Move Chips to The Same Position

def minCostToMoveChips(position):
    hash_chips = {}
    odd_hash = {}
    even_hash = {}
    for chip in position:
        if chip % 2 == 0:
            if chip not in even_hash:
                even_hash[(chip)] = 1
            else:
                even_hash[(chip)] += 1
        else:
            if chip not in odd_hash:
                odd_hash[(chip)] = 1
            else:
                odd_hash[(chip)] += 1
    odd_counter = 0
    even_counter = 0
    for key, value in odd_hash.items():
        odd_counter += value
    for key, value in even_hash.items():
        even_counter += value
    return odd_counter if odd_counter < even_counter else even_counter

print(minCostToMoveChips([1,2,3]))
print(minCostToMoveChips([2,2,2,3,3]))
print(minCostToMoveChips([1,1000000000])) 