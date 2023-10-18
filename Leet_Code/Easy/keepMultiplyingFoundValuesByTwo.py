# Leet Code 2154. Keep Multiplying Found Values by Two

def keepMultiplyingFoundValuesByTwo(nums, original):
    return_val = original
    hashNums = {}
    
    for i in range(len(nums)):
        if nums[i] not in hashNums:
            hashNums[nums[i]] = 1
    
    while True:
        if return_val not in hashNums:
            return return_val
        else:
            return_val = return_val * 2
    
print(keepMultiplyingFoundValuesByTwo([5,3,6,1,12], 3))
print(keepMultiplyingFoundValuesByTwo([2,7,9], 4))