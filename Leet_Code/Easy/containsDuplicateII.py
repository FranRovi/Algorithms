# Leet Code Algo 219. Contains Duplicate II

def containsNearbyDuplicate(nums, k):
    if len(nums) == 1:
        return False
    if len(nums) == len(set(nums)):
        return False
    small_arr = nums[:k+1]
    idx = 0
    while idx + k <= len(nums):
        for i in range(len(small_arr)-1):
            for j in range(i+1,len(small_arr)):
                if small_arr[i] == small_arr[j]:
                    return True
        if k >= len(nums):
            return False
        else:
            idx += 1
            small_arr.pop(0)
            if k + idx == len(nums):
                return False
            else:
                small_arr.append(nums[idx+k])
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([1], 1))
print(containsNearbyDuplicate([1,2], 2))
print(containsNearbyDuplicate([13, 23, 1, 2, 3], 5))
print(containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 1, 10], 15))
        