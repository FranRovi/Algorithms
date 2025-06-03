# Leet Code Algo 2395. Find Subarrays With Equal Sum

def findSubarrays(nums):
    hash_sums = {}
    len_arr = len(nums)
    for i in range(len_arr-1):
        temp = nums[i] + nums[i+1]
        if temp not in hash_sums:
            hash_sums[temp] = (i, i+1)
    for j in range(len_arr-1, 0, -1):
        temp_reverse = nums[j] + nums[j-1]
        if temp_reverse in hash_sums:
            if (hash_sums[temp_reverse][0] != j-1 and hash_sums[temp_reverse][1] != j): 
                return True
    return False  

print(findSubarrays([4,2,4]))
print(findSubarrays([1,2,3,4,5]))
print(findSubarrays([0,0,0]))
