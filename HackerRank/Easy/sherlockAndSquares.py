# Hacker Rank Algo Sherlock and Squares

def sherlockAndSquares(a, b):
    counter = 0
    i = 1
    while i ** 2 <= b:
        i += 1
    for i in range(i + 1):
        if i ** 2 >= a and i ** 2 <= b:
            counter += 1
    return counter
print(sherlockAndSquares(3,9))
print(sherlockAndSquares(17,24))