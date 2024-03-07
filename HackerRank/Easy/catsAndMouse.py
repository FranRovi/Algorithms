# Hacker Rank Cats and Mouse Algo

def catsAndMouse(x, y, z):
    if abs(x - z) > abs(y - z):
        return 'Cat B'
    elif abs(x - z) < abs(y - z):
        return 'Cat A'
    else:
        return 'Mouse C'
print(catsAndMouse(2,5,4))
print(catsAndMouse(1,2,3))
print(catsAndMouse(1,3,2))
    