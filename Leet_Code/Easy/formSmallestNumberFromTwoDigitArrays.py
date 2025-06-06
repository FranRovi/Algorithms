# Leet Code Algo 2605. Form Smallest Number From Two Digit Arrays

def minNumber(nums1, nums2):
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2)

    hash_nums = {}

    for num in sorted_nums1:
        if num not in hash_nums:
            hash_nums[num] = 1 
    for num in sorted_nums2:
        if num not in hash_nums:
            hash_nums[num] = 1
        else:
            hash_nums[num] += 1 

    temp_min_one = int(str(sorted_nums1[0]) + str(sorted_nums2[0]))
    temp_min_two = int(str(sorted_nums2[0]) + str(sorted_nums1[0]))

    min_num = temp_min_one if temp_min_one <= temp_min_two else temp_min_two

    for key, value in hash_nums.items():
        if value == 2 and key < min_num:
            return key
    return min_num

print(minNumber([4,1,3],[5,7]))
print(minNumber([3,5,2,6],[3,1,7]))  
