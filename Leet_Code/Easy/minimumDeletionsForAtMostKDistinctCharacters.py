# Leet Code Algo 3545. Minimum Deletions for At Most K Distinct Characters

def minDeletions(s, k):
    hash_letters = {}
    for i in range(len(s)):
        if s[i] not in hash_letters:
            hash_letters[s[i]] = 1
        else:
            hash_letters[s[i]] += 1
    hash_letters_sorted = dict(sorted(hash_letters.items(), key= lambda item:item[1], reverse=True))
    idx = 1
    total_sum = 0
    for key, value in hash_letters_sorted.items():
        if idx > k:
            total_sum += value
        idx += 1
    return total_sum

print(minDeletions("abc", 2))
print(minDeletions("aabb", 2))
print(minDeletions("yyyzz", 1)) 