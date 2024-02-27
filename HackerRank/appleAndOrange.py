# Hacker Rank Algo Apple and Orange

def countApplesAndOranges(s, t, a, b, apples, oranges):
    counterApples = 0
    counterOranges = 0
    for i in range(len(apples)):
        if apples[i] + a >= s and apples[i] + a <= t:
            counterApples += 1
    for j in range(len(oranges)):
        if oranges[j] + b >= s and oranges[j] + b <= t:
            counterOranges += 1
    print(counterApples)
    print(counterOranges)

countApplesAndOranges(7,11,5,15, [-2,2,1],[5,-6])