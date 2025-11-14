# Leet Code Algo 3740. Minimum Distance Between Three Equal Elements I.

def minimumDistance(nums):
    hash_nums = {}
    for i in range(len(nums)):
        if str(nums[i]) not in hash_nums:
            hash_nums[str(nums[i])] = [i]
        else:
            hash_nums[str(nums[i])].append(i)
    answer = 501
    for key, value in hash_nums.items():
        if len(value) >= 3:
            for j in range(len(value)-2):
                if abs((value[j] - value[j +1])) + abs((value[j+1] - value[j+2])) + abs((value[j+2] - value[j])) < answer:
                    answer = abs((value[j] - value[j +1])) + abs((value[j+1] - value[j+2])) + abs((value[j+2] - value[j]))
    if answer == 501:
        return -1
    return answer

print(minimumDistance([1,2,1,1,3]))
print(minimumDistance([1,1,2,3,2,1,2]))
print(minimumDistance([1]))
