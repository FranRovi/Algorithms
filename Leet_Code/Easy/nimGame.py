# Leet Code Algo 292. Nim Game

def canWinMin(n):
    if n % 4 == 0:
        return False
    return True

print(canWinMin(4))
print(canWinMin(1))
print(canWinMin(2))
print(canWinMin(8))
print(canWinMin(12))
print(canWinMin(9))