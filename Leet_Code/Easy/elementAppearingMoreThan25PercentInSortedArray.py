# Leet Code Algo 1287. Element Appearing More Than 25% in Sorted Array

def findSpecialInteger(arr):
    target_val = int(len(arr) * 0.25)
    hash_nums = {}
    for num in arr:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    for key, value in hash_nums.items():
        if value > target_val:
            return key

print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))
print(findSpecialInteger([1,1]))