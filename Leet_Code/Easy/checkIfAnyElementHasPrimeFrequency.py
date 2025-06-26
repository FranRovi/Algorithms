# Leet Code Algo 3591. Check if Any Element Has Prime Frequency

def checkPrimeFrequency(nums):
    hash_nums_freq = {}
    prime_nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    # prime_nums = [2,3,5,7,11,13,17,19]
    # for i in range(20, 101):
    #     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
    #         continue
    #     else:
    #         prime_nums.append(i) 
    for num in nums:
        if num not in hash_nums_freq:
            hash_nums_freq[num] = 1
        else:
            hash_nums_freq[num] += 1
    for key, value in hash_nums_freq.items():
        if value in prime_nums:
            return True
    return False

print(checkPrimeFrequency([1,2,3,4,5,4]))
print(checkPrimeFrequency([1,2,3,4,5]))
print(checkPrimeFrequency([2,2,2,4,4]))