# Leet Code Algo 3038. Maximum Number of Operations With Same Score I

def maxOperations(nums):
    len_nums = len(nums)
    if len_nums == 2:
        return 1
    else:
        counter = 1
        target_sum = nums[0] + nums[1]
        idx = 2
        while idx < len_nums - 1:
            if nums[idx] + nums[idx+1] == target_sum:
                counter += 1
                idx += 2
            else:
                return counter
        return counter
    
print(maxOperations([3,2,1,4,5]))
print(maxOperations([1,5,3,3,4,1,3,2,2,3]))
print(maxOperations([5,3]))