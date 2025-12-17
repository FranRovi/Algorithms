# Leet Code Algo 3014. Minimum Number of Pushes to Type Word I

def minimumPushes(word):
    hash_chars = {}
    for c in word:
        if c not in hash_chars:
            hash_chars[c] = 1
        else:
            hash_chars[c] += 1
    counter = 0
    total_sum = 0
    for i in range(len(hash_chars)):
        if i % 8 == 0:
            counter += 1
        total_sum += counter
    return total_sum

print(minimumPushes("abcde"))
print(minimumPushes("xycdefghij"))
print(minimumPushes("abhrlngxyjkezwcm"))
print(minimumPushes("bvlqfomhxkpactrjunsidzey"))
print(minimumPushes("amrvxnhsewkoipjyuclgtdbfq"))