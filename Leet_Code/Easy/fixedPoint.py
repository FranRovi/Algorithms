# Leet Code Algo 1064. Fixed Point

def fixedPoint(arr):
    for i in range(len(arr)):
        if i == arr[i]:
            return i
    return -1

print(fixedPoint([-10,-5,0,3,7]))
print(fixedPoint([0,2,5,8,17]))
print(fixedPoint([-10,-5,3,4,7,9]))