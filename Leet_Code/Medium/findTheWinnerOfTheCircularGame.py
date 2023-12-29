# Leet Code Algo 1823. Find the Winner of the Circular Game


def findTheWinnerOfTheCircularGame(n, k):
    playersRem = []
    for i in range(1, n + 1):
        playersRem.append(i)
    idx = 0
    while len(playersRem) > 1:
        if idx + k > len(playersRem) - 1:
            idx = (idx + k - 1) % len(playersRem)
        else:
            idx += k - 1
        playersRem.pop(idx)
    return playersRem[0] 

print(findTheWinnerOfTheCircularGame(5,2))
print(findTheWinnerOfTheCircularGame(6,5))
            