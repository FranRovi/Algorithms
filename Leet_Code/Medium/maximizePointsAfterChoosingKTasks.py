# Leet Code Algo 3767. Maximize Points After Choosing K Tasks.

def maxPoints(technique1, technique2, k):
    max_val = sum(technique1)
    len_arr = len(technique1)
    changes_left = len_arr - k
    if len_arr == k: 
        return max_val
    hash_diff = {}
    for i in range(len_arr):
        temp = technique2[i] - technique1[i]
        if temp not in hash_diff:
            hash_diff[temp] = [i]
        else:
            hash_diff[temp].append(i)
    sort_hash = dict(sorted(hash_diff.items(), reverse = True))
    for key, value in sort_hash.items():
        if key < 1:
            break
        for j in range(len(value)):
            changes_left -= 1
            max_val -= technique1[value[j]]
            max_val += technique2[value[j]]
            if changes_left == 0:
                return max_val 
    return max_val

print(maxPoints([5,2,10],[10,3,8],2))
print(maxPoints([10,20,30],[5,15,25],2))
print(maxPoints([1,2,3],[4,5,6],0))
print(maxPoints([526],[854],1))
print(maxPoints([465,619],[474,109],2))
print(maxPoints([910,729,95,520,658,37,580],[307,586,217,920,402,374,498],5))

