# Hacker Rank Algo. Picking Numbers

def pickingNumbers(a):
    hash_nums = {}
    for i in range(len(a)):
        if a[i] not in hash_nums:
            hash_nums[a[i]] = 1
        else:
            hash_nums[a[i]] += 1     
    if len(hash_nums) == 1:
        return hash_nums[a[0]]
    sorted_hash_nums = dict(sorted(hash_nums.items()))
    sorted_arr_tuple_freq = []
    for key, value in sorted_hash_nums.items():
        sorted_arr_tuple_freq.append((key,value))
    max_num = 0
    for j in range(1, len(sorted_arr_tuple_freq)):
        if sorted_arr_tuple_freq[j][1] > max_num:
            max_num = sorted_arr_tuple_freq[j][1] 
        if sorted_arr_tuple_freq[j-1][0] + 1 == sorted_arr_tuple_freq[j][0]:
            if sorted_arr_tuple_freq[j-1][1] + sorted_arr_tuple_freq[j][1] > max_num:
                max_num = sorted_arr_tuple_freq[j-1][1] + sorted_arr_tuple_freq[j][1]
    return max_num
    
print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
print(pickingNumbers([4,6,5,3,3,1]))
print(pickingNumbers([1,2,2,3,1,2]))
print(pickingNumbers([66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66]))
print(pickingNumbers([4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]))

    