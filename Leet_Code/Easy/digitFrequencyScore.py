# Leet Code Algo 3945. Digit Frequency Score.

def digitFrequencyScore(n):
    str_num = str(n)
    hash_freq = {}
    for c in str_num:
        if c not in hash_freq:
            hash_freq[c] = 1
        else:
            hash_freq[c] += 1
    total_sum = 0
    for key, value in hash_freq.items():
        total_sum += int(key) * value
    return total_sum

print(digitFrequencyScore(122))
print(digitFrequencyScore(101))
print(digitFrequencyScore(7917))