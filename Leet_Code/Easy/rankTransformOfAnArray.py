# Leet Code Algo 1331. Rank Transform of an Array

def arrayRankTransform(arr):
    len_arr = len(arr)
    if len_arr == 0:
        return []
    sorted_arr = sorted(arr)
    hash_nums = {}
    idx = 1
    for i in range(len(sorted_arr)):
        if sorted_arr[i] not in hash_nums:
            hash_nums[sorted_arr[i]] = idx
            idx += 1
    answer = []
    for j in range(len_arr):
        answer.append(hash_nums[arr[j]])
    return answer

print(arrayRankTransform([40,10,20,30]))
print(arrayRankTransform([100,100,100]))
print(arrayRankTransform([37,12,28,9,100,56,80,5,12]))