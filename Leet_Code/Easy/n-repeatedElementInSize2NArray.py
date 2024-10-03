# Leet Code Algo 961. N-Repeated Element in Size 2N Array

def repeatedNTimes(nums):
    hashNums = {}
    for num in nums:
        if num not in hashNums:
            hashNums[num] = 1
        else:
            hashNums[num] += 1
    for key, value in hashNums.items():
        if value == (len(nums) / 2):
            return key

print(repeatedNTimes([1,2,3,3]))
print(repeatedNTimes([2,1,2,5,3,2]))
print(repeatedNTimes([5,1,5,2,5,3,5,4]))