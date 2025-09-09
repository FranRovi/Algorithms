# Leet Code Algo 2379. Minimum Recolors to Get K Consecutive Black Blocks

def minimumRecolors(blocks, k):
    temp = list(blocks[:k])
    temp_white = 0
    min_max = 0
    for i in range(k):
        if temp[i] == "W":
            temp_white += 1
    if temp_white > min_max:
        min_max = temp_white
    for j in range(k, len(blocks)):
        if blocks[j] == "W":
            temp_white += 1
        if temp[0] == "W":
            temp_white -= 1
        if temp_white < min_max:
            min_max = temp_white
        temp.append(blocks[j])
        temp.pop(0)
    return min_max

print(minimumRecolors("WBBWWBBWBW",7))
print(minimumRecolors("WBWBBBW",2))
print(minimumRecolors("W",1))
print(minimumRecolors("BWBBWWBBBWBWWWBWWBBWBWBBWBB",11))