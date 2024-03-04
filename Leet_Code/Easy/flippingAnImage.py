# Leet Code Algo 832. Flipping an Image

def flippingAnImage(image):
    reversedImage = []
    for i in range(len(image)):
        reversedArr = []
        tempArr = image[i]
        for j in range(len(tempArr) -1, -1, -1):
            if tempArr[j] == 0:
                reversedArr.append(1)
            else:
                reversedArr.append(0)
        reversedImage.append(reversedArr)
    return reversedImage

print(flippingAnImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flippingAnImage([[1,1,0,0],[1,0,0,1],[1,0,1,0]]))