# Leet Code Algo 1791. Find Center of Star Graph

def findCenterOfStarGraph(edges):
    eleOne = edges[0][0]
    eleTwo = edges[0][1]
    return eleOne if eleOne in edges[1] else eleTwo

print(findCenterOfStarGraph([[1,2], [2,3], [4,2]]))
print(findCenterOfStarGraph([[1,2], [5,1], [1,3], [1,4]]))