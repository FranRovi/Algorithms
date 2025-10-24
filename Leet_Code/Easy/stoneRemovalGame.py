# Leet Code Algo 3360. Stone Removal Game

def canAliceWin(n):
    counter = 1
    for i in range(10, 0, -1):
        if n - i < 0:
            break
        n -= i
        counter += 1
    return True if counter % 2 == 0 else False

print(canAliceWin(12))
print(canAliceWin(1))
print(canAliceWin(10))
print(canAliceWin(19))