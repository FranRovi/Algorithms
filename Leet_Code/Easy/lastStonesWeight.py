# Leet Code Algo 1046. Last Stone Weight

def lastStoneWeight(stones):
    while len(stones):
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        largest = -1
        idxLargest = 0
        secondLargest = -1
        idxSecondLargest = 0
        for i in range(len(stones)):
            if stones[i] > largest:
                secondLargest = largest
                idxSecondLargest = idxLargest
                idxLargest = i
                largest = stones[i]
            elif stones[i] <= largest and stones[i] >= secondLargest:
                idxSecondLargest = i
                secondLargest = stones[i]    
        # print(stones, len(stones))
        if idxLargest < idxSecondLargest:
            del stones[idxLargest]
            del stones[idxSecondLargest - 1]
        else:
            del stones[idxSecondLargest]
            del stones[idxLargest - 1]
        stones.append(largest - secondLargest)
    return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))
print(lastStoneWeight([3,1]))
print(lastStoneWeight([4,3,4,3,2]))
print(lastStoneWeight([3,7,8]))
print(lastStoneWeight([9,3,2,10])) 
            