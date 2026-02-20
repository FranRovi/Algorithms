# Leet Code Algo 3842. Toogle Light Bulbs

def toggleLightBulbs(bulbs):
    hash_bulbs = {}
    for b in bulbs:
        if str(b) not in hash_bulbs:
            hash_bulbs[str(b)] = 1
        else:
            hash_bulbs[str(b)] += 1
    answer = []
    for key, value in hash_bulbs.items():
        if value % 2 != 0:
            answer.append(int(key))
    return sorted(answer)

print(toggleLightBulbs([10,30,20,10]))
print(toggleLightBulbs([100,100]))