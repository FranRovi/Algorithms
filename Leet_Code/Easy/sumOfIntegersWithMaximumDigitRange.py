# Leet Code Algo 3982. Sum of Integers with Maximum Digit Range.

def findMinMax(n):
        n_list = [int(digit) for digit in str(n)] 
        sorted_list = sorted(n_list)
        return sorted_list[-1] - sorted_list[0]
    
def maxDigitRange(nums: list[int]) -> int:
    hash_difference = {}
    for n in nums:
        temp = findMinMax(n)
        if temp not in hash_difference:
            hash_difference[temp] = [n]
        else:
            hash_difference[temp].append(n)
    sorted_hash_diff = dict(sorted(hash_difference.items(), key=lambda item: item[0], reverse=True))
    total_sum = 0
    for key, value in sorted_hash_diff.items():
        for i in range(len(value)):
            total_sum += value[i]
        break
    return total_sum

print(maxDigitRange([5724,111,350]))
print(maxDigitRange([90,900]))
print(maxDigitRange([76207,65921]))
