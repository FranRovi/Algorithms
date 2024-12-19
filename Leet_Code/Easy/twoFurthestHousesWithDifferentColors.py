# Leet Code Algo 2078. Two Furthest Houses With Different Colors

def maxDistance(colors):
    maxDistance = 0
    for i in range(len(colors)):
        for j in range(i+1, len(colors)):
            if colors[i] != colors[j]:
                if maxDistance < abs(i - j):
                    maxDistance = abs(i - j)
    return maxDistance

print(maxDistance([1,1,1,6,1,1,1]))
print(maxDistance([1,8,3,8,3]))
print(maxDistance([0,1]))
print(maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))