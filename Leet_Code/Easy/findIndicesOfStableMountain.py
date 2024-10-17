# Leet Code Algo 3285. Find Indices of Stable Mountain

def stableMountains(height, threshold):
    indices = []
    for i in range(1, len(height)):
        if height[i-1] > threshold:
            indices.append(i)
    return indices

print(stableMountains([1,2,3,4,5],2))
print(stableMountains([10,1,10,1,10],3))
print(stableMountains([10,1,10,1,10],10))