# Leet Code Algo 3861. Minimum Capacity Box

def minimumIndex(capacity, itemSize):
    min_box = 101
    min_idx = 0
    for i in range(len(capacity)):
        if capacity[i] < min_box and capacity[i] >= itemSize:
            min_box = capacity[i]
            min_idx = i
    if min_box != 101:
        return min_idx
    else:
        return -1
    
print(minimumIndex([1,5,3,7], 3))
print(minimumIndex([3,5,4,3], 2))
print(minimumIndex([4], 5))