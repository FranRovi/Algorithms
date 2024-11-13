# Leet Code Algo 1779. Find Nearest Point That Has the Same X or Y Coordinate

def nearestValidPoint(x, y, points):
    minDistance = 99999
    minIdx = 99999
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            tempDist = abs(points[i][0] - x) + abs(points[i][1] - y)
            if tempDist < minDistance:
                minDistance = tempDist
                minIdx = i
    if minDistance != 99999:
        return minIdx
    else:
        return -1
print(nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
print(nearestValidPoint(3,4,[[3,4]]))
print(nearestValidPoint(3,4,[[2,3]]))