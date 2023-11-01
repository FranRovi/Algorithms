# Leet Code 1732. Find The Highest Altitude 

def findTheHighestAltitude(gain):
    maxHeightGain = 0
    arrHeightGain = [0]
    currentHeight = 0
    for i in range(len(gain)):
        currentHeight += gain[i]
        arrHeightGain.append(currentHeight)
        if maxHeightGain < currentHeight:
            maxHeightGain = currentHeight
    return maxHeightGain
print(findTheHighestAltitude([-5,1,5,0,-7]))
print(findTheHighestAltitude([-4,-3,-2,-1,4,3,2]))
    