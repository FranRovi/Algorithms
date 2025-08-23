# Leet Code Algo 1852. Distinct Numbers in Each Subarray

def distinctNumbers(nums, k):
    len_nums = len(nums)
    temp = nums[:k]
    len_arr_of_sub_arr = len_nums - k + 1
    answer = [0] * len_arr_of_sub_arr
    hash_nums = {}
    for l in range(k):
        if temp[l] not in hash_nums:
            hash_nums[temp[l]] = 1
        else:
            hash_nums[temp[l]] += 1
    size_hash = len(hash_nums)
    answer[0] = size_hash
    idx = 1
    for i in range(k, len_nums):
        temp.append(nums[i])
        if nums[i] not in hash_nums:
            hash_nums[nums[i]] = 1
            size_hash += 1
        else:
            hash_nums[nums[i]] += 1
        ele_to_del = temp[0]
        temp.pop(0)
        if hash_nums[ele_to_del] == 1:
            del hash_nums[ele_to_del]
            size_hash -= 1 
        else:
            hash_nums[ele_to_del] -= 1
        answer[idx] = size_hash
        idx += 1 
    return answer

print(distinctNumbers([1,2,3,2,2,1,3], 3))
print(distinctNumbers([1,1,1,1,2,3,4], 4))