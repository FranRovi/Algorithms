# Leet Code Algo 3931. Check Adjacent Digit Differences.

def isAdjacentDiffAtMostTwo(s):
    s_list = list(map(int, str(s)))
    for i in range(1, len(s_list)):
        if abs(s_list[i-1] - s_list[i]) > 2:
            return False
    return True

print(isAdjacentDiffAtMostTwo("132"))
print(isAdjacentDiffAtMostTwo("129"))
        