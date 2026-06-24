# Leet Code Algo 3968. Maximum Manhattan Distance After All Moves

def maxDistance(moves):
    counter_up = 0
    counter_right = 0
    counter_joker = 0
    for c in moves:
        match c:
            case "U":
                counter_up += 1
            case "D":
                counter_up -= 1
            case "R":
                counter_right += 1
            case "L":
                counter_right -= 1
            case "_":
                counter_joker += 1
    return abs(counter_right) + abs(counter_up) + counter_joker

print(maxDistance("L_D_"))
print(maxDistance("U_R"))