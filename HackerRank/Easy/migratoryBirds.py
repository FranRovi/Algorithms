# Hacker Rank Algo. Migratory Birds

def migratoryBirds(arr):
    birdsHash = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
    }
    for i in range(len(arr)):
        if arr[i] in birdsHash:
            birdsHash[arr[i]] += 1
    sortedBirdsByValue = sorted(birdsHash.items(), key=lambda x:x[1], reverse=True)
    birdHashSorted = dict(sortedBirdsByValue)
    for key in birdHashSorted.items():
        return key[0]

print(migratoryBirds([1,4,4,4,5,3]))
print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4]))
# 