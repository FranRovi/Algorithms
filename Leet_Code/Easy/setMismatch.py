# Leet Code Algo 645. Set Mismatch

def findErrorNums(nums):
    hash_nums = {}
    answer = []
    low_val = nums[0]
    high_val = nums[0]
    missing_number = -1
    for i in range(len(nums)):
        if nums[i] not in hash_nums:
            hash_nums[nums[i]] = 1
            if nums[i] > high_val:
                high_val = nums[i]
            if nums[i] < low_val:
                low_val = nums[i]   
        else:
            hash_nums[nums[i]] += 1
            if nums[i] > high_val:
                high_val = nums[i]
            if nums[i] < low_val:
                low_val = nums[i]   
    idx = 1
    for key, value in hash_nums.items():
        if value == 2:
            answer.insert(0, key)
        if idx not in hash_nums:
            missing_number = idx
            answer.append(missing_number)
        idx += 1
    if missing_number == -1:
        answer.append(high_val + 1)
    return answer

print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))
print(findErrorNums([3,2,2]))