# Leet Code Algo 2833. Furthest Point from Origin 

def furthestDistanceFromOrigin(moves):
    countL = 0
    countR = 0
    countUnderscore = 0
    
    for i in range(len(moves)):
        if moves[i] == 'L':
            countL += 1
        elif moves[i] == 'R':
            countR += 1
        else:
            countUnderscore += 1
    if countL > countR:
        return countL + countUnderscore - countR
    else:
        return countR + countUnderscore - countL
        

print(furthestDistanceFromOrigin("L_RL__R"))
print(furthestDistanceFromOrigin("_R__LL_"))
print(furthestDistanceFromOrigin("_______"))
                