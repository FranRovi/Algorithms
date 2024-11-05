# Leet Algo 3069. Distribute Elements Into Two Arrays I

def resultArray(nums):
    arrOne = [nums[0]]
    arrTwo = [nums[1]]
    for i in range(2, len(nums)):
        if arrOne[-1] > arrTwo[-1]:
            arrOne.append(nums[i])
        else:
            arrTwo.append(nums[i])
    return arrOne + arrTwo

print(resultArray([2,1,3]))
print(resultArray([5,4,3,8]))