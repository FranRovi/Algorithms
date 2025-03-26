# Leet Code Algo 1426. Counting Elements

def countElements(nums):
    counter = 0
    hash_nums = {}
    for num in nums:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    for key, value in hash_nums.items():
        if key + 1 in hash_nums:
            counter += value
    return counter

print(countElements([1,2,3]))
print(countElements([1,1,3,3,5,5,7,7]))
print(countElements([1,3,2,3,5,0]))
print(countElements([1,1,2,2]))            
    