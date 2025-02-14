# Leet Code Algo 3442. Maximum Difference Between Even and Odd Frequency I

def maxDifference(s):
    hash_frequency = {}
    for i in range(len(s)):
        if s[i] not in hash_frequency:
            hash_frequency[s[i]] = 1
        else:
            hash_frequency[s[i]] += 1
    max_odd = 0
    min_even = 99999
    for key, value in hash_frequency.items():
        if value % 2 == 0:
            if value < min_even:
                min_even = value
        else:
            if value > max_odd:
                max_odd = value
    return max_odd - min_even

print(maxDifference("aaaaabbc"))
print(maxDifference("abcabcab"))