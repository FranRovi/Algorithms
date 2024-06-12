# Leet Code Algo 1812. Determine Color of a Chessboard Square

def isSquareWhite(coordinates):
    letters = {"a", "c", "e", "g"}
    letter = coordinates[0]
    num = int(coordinates[-1])
    if letter in letters and num % 2 != 0:
        return False
    if letter not in letters and num % 2 == 0:
            return False
    return True

print(isSquareWhite("a1"))
print(isSquareWhite("h3"))
print(isSquareWhite("c7"))
print(isSquareWhite("e5"))
print(isSquareWhite("d7"))
 