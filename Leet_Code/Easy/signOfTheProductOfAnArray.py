# Leet Code Algo 1822. Sign of the Product of an Array

def signFunc(x):
    if x > 0:
            return 1
    elif x < 0:
        return -1
    else:
        return 0
    
def signOfTheProductOfAnArray(nums):
    totalProd = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            # print(0)
            return 0
        else:
            totalProd *= nums[i]
    return signFunc(totalProd)

print(signOfTheProductOfAnArray([-1,-2,-3,-4,3,2,1]))
print(signOfTheProductOfAnArray([1,5,0,2,-3]))
print(signOfTheProductOfAnArray([-1,1,-1,1,-1]))