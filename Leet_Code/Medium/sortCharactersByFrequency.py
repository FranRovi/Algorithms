# Leet Code Algo 451. Sort Characters By Frequency

def frequencySort(s):
    hash_freq = {}
    for char in s:
        if char not in hash_freq:
            hash_freq[char] = 1
        else:
            hash_freq[char] += 1
    sorted_items = sorted(hash_freq.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_items)
    answer = ""
    for key, value in sorted_dict.items():
            answer += key * value
    return answer

print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))