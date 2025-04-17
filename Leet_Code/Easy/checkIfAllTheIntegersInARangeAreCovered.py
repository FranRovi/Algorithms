# Leet Code Algo 1893. Check if All the Integers in a Range are Covered

def isCovered(ranges, left, right):
    interval_covered = set()
    for i in range(len(ranges)):
        for j in range(ranges[i][0], ranges[i][1] + 1):
            interval_covered.add(j)
    for k in range(left, right + 1):
        if k not in interval_covered:
            return False
    return True

print(isCovered([[1,2],[3,4],[5,6]], 2, 5))
print(isCovered([[1,10],[10,20]], 21, 21))
print(isCovered([[1,1]], 1, 50))
print(isCovered([[37,49],[5,17],[8,32]], 29, 49))