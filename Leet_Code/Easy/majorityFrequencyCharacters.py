# Leet Code Algo 3692. Majority Frequency Characters

def majorityFrequencyGroup(s):
    hash_chars = {}
    for char in s:
        if char not in hash_chars:
            hash_chars[char] = 1
        else:
            hash_chars[char] += 1
    hash_freq = {}
    for key, value in hash_chars.items():
        if str(value) not in hash_freq:
            hash_freq[str(value)] = [key]
        else:
            hash_freq[str(value)].append(key)
    sorted_freq = dict(sorted(hash_freq.items(), key=lambda item: (len(item[1]),item[0]), reverse=True))
    for key, value in sorted_freq.items():
        return "".join(value)
    
print(majorityFrequencyGroup("aaabbbccdddde"))
print(majorityFrequencyGroup("abcd"))
print(majorityFrequencyGroup("pfpfgi"))
print(majorityFrequencyGroup("asrhyrmzhcehcydmrmce"))
    