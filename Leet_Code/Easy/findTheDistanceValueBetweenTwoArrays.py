# Leet Code Algo 1385. Find the Distance Value Between Two Arrays.

def findTheDistanceValue(arr1, arr2, d):
    counter = 0
    is_valid = True
    for num in arr1:
        for n in arr2:
            if abs(num - n) <= d:
                is_valid = False
                break
        if is_valid:
            counter += 1
        is_valid = True
    return counter   

print(findTheDistanceValue([4,5,8],[10,9,1,8],2)) 
print(findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3)) 
print(findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7],6)) 