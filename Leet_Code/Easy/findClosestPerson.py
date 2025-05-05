# Leet Code Algo 3516. Find Closest Person

def findClosest(x, y, z):
    dif_one = abs(x-z)
    dif_two = abs(y-z)
    if dif_one < dif_two:
        return 1
    elif dif_one == dif_two:
        return 0     
    else:
        return 2

print(findClosest(2,7,4))
print(findClosest(2,5,6))
print(findClosest(1,5,3))   