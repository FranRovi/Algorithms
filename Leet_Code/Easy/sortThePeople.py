# Leet Code Algo 2418. Sort the People

def sortThePeople(names, heights):
    heightTupleArr = []
    orderHeightNameArr = []
    
    for i in range(len(names)):
        temp = names[i],heights[i]
        heightTupleArr.append(temp)
    
    sortedPeopleByHeight = sorted(heightTupleArr, key=lambda x : x[1], reverse = True)
    for i in range(len(sortedPeopleByHeight)):
        name = sortedPeopleByHeight[i][0]
        orderHeightNameArr.append(name)
        
    return orderHeightNameArr

print(sortThePeople(["Mary", "John", "Emma"], [180, 165, 170]))
print(sortThePeople(["Alice", "Bob", "Bob"], [155, 185, 150]))