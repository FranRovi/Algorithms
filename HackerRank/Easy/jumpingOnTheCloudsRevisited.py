# Hacker Rank Algo Jumping On The Clouds Revisited

def jumpingOnTheClouds(c, k):
    energyLevel = 100
    idx = k
    while idx % len(c) != 0:
        energyLevel -= 1
        if c[idx%len(c)] == 1:
            energyLevel -= 2
        idx += k
    if c[0] == 1:
        energyLevel -= 2
    energyLevel -= 1
    return energyLevel
        
            
print(jumpingOnTheClouds([0,0,1,0,0,1,1,0],2))
print(jumpingOnTheClouds([1,1,1,0,1,1,0,0,0,0],3))
        