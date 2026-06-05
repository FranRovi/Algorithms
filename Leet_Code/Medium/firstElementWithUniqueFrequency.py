# Leet Code Algo 3843. First Element with Unique Frequency.

def firstUniqueFreq(nums):
    hash_nums = {}
    for n in nums:
        if n not in hash_nums:
            hash_nums[n] = 1
        else:
            hash_nums[n] += 1
    hash_frequency = {}
    for key, value in hash_nums.items():
        if value not in hash_frequency:
            hash_frequency[value] = [key]
        else:
            hash_frequency[value].append(key)
    for key, value in hash_frequency.items():
        if len(value) == 1:
            return value[0]
    return -1

print(firstUniqueFreq([20,10,30,30]))
print(firstUniqueFreq([20,20,10,30,30,30]))
print(firstUniqueFreq([10,10,20,20]))