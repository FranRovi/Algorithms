# Leet Code Algo 3158. Find the XOR of Numbers Which Appear Twice

def duplicateNumbersXOR(nums):
    hash_nums = {}
    answer = 0
    for (n) in nums:
        if (n) not in hash_nums:
            hash_nums[(n)] = 1
        else:
            answer ^= n
    return answer

print(duplicateNumbersXOR([1,2,1,3]))
print(duplicateNumbersXOR([1,2,3]))
print(duplicateNumbersXOR([1,2,2,1]))