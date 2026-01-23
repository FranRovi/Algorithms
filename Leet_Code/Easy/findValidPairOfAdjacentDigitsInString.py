# Leet Code Algo 3438. Find Valid Pair of Adjacent Digits in String

import itertools

def findValidPair(s):
    if len(s) < 2:
        return ""
    hash_nums = {}
    for num in s:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1
    keys_to_del = []
    for key, value in hash_nums.items():
        if int(key) != value:
            keys_to_del.append(key)
    for num in keys_to_del:
        del hash_nums[num]
    pairs = []
    for i in range(1, len(s)):
        pairs.append("".join(s[i-1] + s[i]))
    valid_keys_arr = list(hash_nums.keys())
    perms = itertools.permutations(valid_keys_arr, r=2)
    perm_arr = []
    for p in perms:
        perm_arr.append("".join(p))
    for j in range(len(pairs)):
        if pairs[j] in perm_arr:
            return pairs[j]
    return ""

print(findValidPair("2523533"))
print(findValidPair("221"))
print(findValidPair("22"))
print(findValidPair("4833931444"))
print(findValidPair("93723239"))
print(findValidPair("24314474"))
print(findValidPair("1522"))
print(findValidPair("12597319494953859992349459"))