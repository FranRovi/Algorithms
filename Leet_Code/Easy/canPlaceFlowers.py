# Leet Code 605. Can Place Flowers

def canPlaceFlowers(flowerbed, n):
    counter = 0
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True
    if len(flowerbed) >= 2:
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            counter += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            counter += 1     
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            counter += 1
    return True if counter >= n else False 


print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,0,1], 2))
print(canPlaceFlowers([0,0,1,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1,0,0], 2))