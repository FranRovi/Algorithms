# Leet Code Algo 3940. Limit Occurrences in Sorted Array.

def limitOccurrences(nums, k):
    hash_nums = {}
    for num in nums:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    answer = []
    smallest = 0
    for key, value in hash_nums.items():
        if value > k:
            for j in range(k):
                answer.append(key)
        else:
            for j in range(value):
                answer.append(key)
    return answer

print(limitOccurrences([1,1,1,2,2,3], 2))
print(limitOccurrences([1,2,3], 1))