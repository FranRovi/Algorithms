# Leet Code Algo 492. Construct the Rectangle

import math

def constructRectangle(area):
    sqroot = math.ceil(area ** 0.5)
    if sqroot * sqroot == area:
        return [sqroot, sqroot]
    for i in range(sqroot + 1, 0, -1):
        if area % i == 0:
            if i < int(area / i):
                return [int(area / i), i]
            else:
                return [i, int(area / i)]

print(constructRectangle(4))
print(constructRectangle(37))
print(constructRectangle(122122))
print(constructRectangle(2))

     