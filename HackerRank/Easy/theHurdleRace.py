# Hacker Rank The Hurdel Race

def theHurdleRace(k, height):
    tallest = height[0]
    for i in range(1, len(height)):
        if height[i] > tallest:
            tallest = height[i]
    if tallest > k:
        return tallest - k
    else:
        return 0
    
print(theHurdleRace(4,[1,6,3,5,2]))
print(theHurdleRace(7,[2,5,4,5,2]))
