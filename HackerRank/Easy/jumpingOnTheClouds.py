# Hacker Rank Algo Jumping on the Clouds

def jumpingOnTheClouds(c):
    counter = 0
    idx = 0
    while idx < len(c) - 2:
        #print(idx)
        if c[idx + 2] == 0:
            idx += 1
        idx += 1
        counter += 1
    if len(c) - idx > 1:
        counter += 1 
    return counter
    
print(jumpingOnTheClouds([0,1,0,0,0,1,0]))
print(jumpingOnTheClouds([0,0,1,0,0,1,0]))
print(jumpingOnTheClouds([0,0,0,0,1,0]))
print(jumpingOnTheClouds([0,0,0,1,0,0]))
         