# Leet Code 657. Robot Return to Origin

def robotReturnToOrigin(moves):
    if len(moves) % 2 != 0:
        return False
    movesArr = [0,0,0,0]
    for i in range(len(moves)):
        if moves[i] =="U":
            movesArr[0] += 1
        elif moves[i] =="D":
            movesArr[1] += 1
        elif moves[i] =="L":
            movesArr[2] += 1
        elif moves[i] =="R":
            movesArr[3] += 1
    if (movesArr[0] == movesArr[1] and
        movesArr[2] == movesArr[3]):
        return True
    return False

print(robotReturnToOrigin("UD"))
print(robotReturnToOrigin("LL"))
print(robotReturnToOrigin("UDLLRR"))
print(robotReturnToOrigin("UDLLRRR"))