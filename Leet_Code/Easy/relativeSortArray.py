# Leet Code Algo 1122. Relative Sort Array.

def relativeSortArray(arr1, arr2):
    hash_arr_one = {}
    single_arr_nums = []
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            single_arr_nums.append(arr1[i])
        if arr1[i] not in hash_arr_one:
            hash_arr_one[arr1[i]] = 1
        else:
            hash_arr_one[arr1[i]] += 1
    answer = []
    for j in range(len(arr2)):
        temp = hash_arr_one[arr2[j]]
        for k in range(temp):
            answer.append(arr2[j])
    sorted_single_nums_arr = sorted(single_arr_nums)
    for n in sorted_single_nums_arr:
        answer.append(n)
    return answer

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
print(relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))