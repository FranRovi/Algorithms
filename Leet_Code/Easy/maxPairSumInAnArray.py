# Leet Code Algo 2815. Max Pair Sum in an Array

def maxSum(nums):
    hashLargestDigit = {}
    largestDigit = 0
    for i in range(len(nums)):
        tempNumStr = str(nums[i])
        for j in range(len(tempNumStr)):
            if int(tempNumStr[j]) > largestDigit:
                largestDigit = int(tempNumStr[j])
        if largestDigit not in hashLargestDigit:
            hashLargestDigit[largestDigit] = [int(tempNumStr)]
        else:
            hashLargestDigit[largestDigit].append(int(tempNumStr))
        largestDigit = 0
    sortedDictByKeyTup = sorted(hashLargestDigit.items(), key=lambda x:x, reverse=True)
    sorted_keys_dec = dict(sortedDictByKeyTup)
    max_value = 0
    for key, value in sorted_keys_dec.items():
        if len(value) > 1:
            sorted_value = sorted(value, reverse = True)
            if sorted_value[0] + sorted_value[1] > max_value:
                max_value = sorted_value[0] + sorted_value[1]
    if max_value != 0:
        return max_value
    else:
        return -1

print(maxSum([112,131,411]))
print(maxSum([2536,1613,3366,162]))
print(maxSum([51,71,17,24,42]))
print(maxSum([84,91,18,59,27,9,81,33,17,58]))