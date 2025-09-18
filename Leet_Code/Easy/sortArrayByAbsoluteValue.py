# Leet Code Algo 3667. Sort Array By Absolute Value

def sortByAbsoluteValue(nums):
    hash_nums = {}
    for i in range(len(nums)):
        if nums[i] not in hash_nums:
            if nums[i] < 0:
                hash_nums[nums[i]] = [nums[i] * -1,1]
            else:
                hash_nums[nums[i]] = [nums[i],1]
        else:
            hash_nums[nums[i]][1] += 1
    sorted_dict = dict(sorted(hash_nums.items(), key=lambda x:x[1]))
    answer = []
    for key, value in sorted_dict.items():
        for j in range(value[1]):
            answer.append(key)
    return answer

print(sortByAbsoluteValue([3,-1,-4,1,5]))
print(sortByAbsoluteValue([-100,100]))
print(sortByAbsoluteValue([-2,-2]))