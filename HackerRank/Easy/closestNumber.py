# Hacker Rank Algo. Closest Number

def closestNumber(arr):
    sortedArr = sorted(arr)
    minDiff = 9999999
    answer = []
    print(sortedArr)
    for i in range(1, len(sortedArr)):
        print(minDiff)
        if minDiff > abs(sortedArr[i] - sortedArr[i-1]):
            minDiff = abs(sortedArr[i] - sortedArr[i-1])
            answer = []
            answer.append(sortedArr[i-1])
            answer.append(sortedArr[i])
        elif minDiff == abs(sortedArr[i] - sortedArr[i-1]):
            answer.append(sortedArr[i-1])
            answer.append(sortedArr[i])
    print(minDiff)
    return answer

print(closestNumber([5,4,3,2,1]))
print(closestNumber([-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854 ]))
# print(closestNumber([]))
# print(closestNumber([5,4,3,2,1]))

