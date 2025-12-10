# Leet Code Algo 3769. Sort Integers by Binary Reflection

def intToBit(n):
    reversedBit = []
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    str_num = ""
    for ele in reversedBit:
        str_num += str(ele)
    return str_num 

    
def sortByReflection(nums):
    hash_bin_nums = {}
    for i in range(len(nums)):
        temp = intToBit(nums[i])
        if str(nums[i]) in hash_bin_nums:
            hash_bin_nums[str(nums[i])][1] += 1
        else:
            hash_bin_nums[str(nums[i])] = [int(temp), 1]
    sorted_hash_bin_nums = dict(sorted(hash_bin_nums.items(), key=lambda item: (item[1][0], int(item[0]))))
    answer = []
    for key, value in sorted_hash_bin_nums.items():
        for j in range(value[1]):
            answer.append(int(key))
    return answer

print(sortByReflection([4,5,4]))
print(sortByReflection([3,6,5,8]))