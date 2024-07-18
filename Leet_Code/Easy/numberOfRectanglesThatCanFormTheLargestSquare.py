# Leet Code Algo 1725. Number of Rectangles That Can Form The Largest Square

def countGoodRectangles(rectangles):
    maxRect = 0
    count = 0
    for i in range(len(rectangles)):
        if rectangles[i][0] > rectangles[i][1]:
            maxTemp = rectangles[i][1]
        else:
            maxTemp = rectangles[i][0]
        if maxTemp > maxRect:
            maxRect = maxTemp
            count = 1
        elif maxTemp == maxRect:
            count += 1
    return count

print(countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))
print(countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]))